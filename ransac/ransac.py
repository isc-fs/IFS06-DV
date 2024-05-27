"""
================
ransac.py (v1.1)
================

Elaborada por Sergio Jimenez Romero para el ISC
Permite aplicar el algoritmo de RANSAC a un conjunto de datos
No se ha usado la implementacion de sklearn porque es muy lenta
(se puede comprobar en los test)
***ATENCION***
La version actual solo se ha probado en 2 dimensiones y en 3 dimensiones. Si
se quisiera extender a mas dimensiones puede que se tengan que hacer mas cambios,
sobre todo en la version de numba

Actualizaciones v1.1:
- Cambio de MSE a MAD y cambio de error cuadrático a error absoluto. Usar
  el error cuadratico y el MSE daba problemas cuando la ultima dimension 
  no era la de mayor variación
- Se devuelven los coeficintes definitivos además de los puntos que son inliers
"""

# Dependencias
import numpy as np
import numba
from numba.np.extensions import cross2d
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
import timeit
from time import time


def ransac(data, m=3, prob=0.9999, threshold=None, max_iter=15000, rot=False):
    """
    Aplica el algoritmo de RANSAC para separar los outliers de los
    inliers en un conjunto de datos dado

    Args:
        data (np.ndarray): Array con los datos
        m (int, optional): Numero de puntos con los que se define el hiperplano (numero minimo de
                           puntos para poder hacer un ajuste). Defaults to 3.
        prob (float, optional): Proabilidad de que el subset de puntos no tenga outliers. Defaults to 0.99.
        threshold (float, optional): Punto a partir del cual un punto no se considera que esta bien ajustado por el hiperplano.
                                     Se le da un valor de None para que se calcule el valor automatico. Defaults to None.
        max_iter (int, optional): Iteraciones maximas. Defaults to 15000.

    Returns:
        np.ndarray, np.ndarray: Devuelve las posiciones de los puntos que se consideran inliers y los coeficinetes definitivos
    """
    if not threshold:
        # He usado el MAD (median absolute deviation) igual que sklearn. Usamos
        # error absoluto
        threshold = np.median(np.abs(data[:, -1] - np.median(data[:, -1])))

    # Añadimos una columna de unos para el sesgo
    A = np.c_[np.ones(data.shape[0]), data]
    # Cota inferior del numero de iteraciones para garantizar la probabilidad
    k = max_iter
    support = 1
    # Iteraciones hechas
    iters = 0
    data_size = len(data)
    # Los coeficientes del hiperplano definitivo
    def_coefs = None
    # Ejecutamos hasta que hayamos hecho mas iteraciones de las necesarias
    while iters < k:
        # Escogemos m puntos al azar
        points_ind = np.random.choice(data_size, m, replace=False)
        points = A[points_ind]
        # Obtenemos los parametros del hiperplano usando descomposicion en valores singulares
        _, _, Vt = np.linalg.svd(points)
        coefs = Vt[-1, :]

        # Cuantos puntos son inliers
        coefs_div = coefs[:-1] / (-1 * coefs[-1])
        support_aux = (
            np.sum(np.abs(A[:, :-1].dot(coefs_div) - A[:, -1]) < threshold) - m
        )
        # Si es el mejor hasta ahora nos guardamos
        if support_aux > support:
            support = support_aux
            def_coefs = coefs
            k = np.log(1 - prob) / np.log(1 - (support / data_size) ** m)
        iters += 1
    if def_coefs[-1] < 0:
        def_coefs = -1 * def_coefs
    return (
        np.where(
            np.abs(A[:, :-1].dot(def_coefs[:-1] / (-1 * def_coefs[-1])) - A[:, -1])
            < threshold
        ),
        def_coefs,
    )


@numba.jit(nopython=True)
def ransac2(data, m=3, prob=0.999, threshold=None, max_iter=15000):
    """
    Funciona exactamente igual que la funcion anterior, pero utiliza numba
    Esto da una ligera mejora en el rendimiento, pero por facilidad de cambiar
    lo mejor yo creo que es utilizar la anterior y solo recurrir a esta si necesitamos
    rendimiento. Se le tiene tambien que pasar la matriz ya transformada porque
    numba no funciona bien con np.stack. Tambien tarda bastante mas la primera vez que se ejecuta

    Args:
        data (np.array): Los datos con la columna de 1s para el sesgo
        m (int, optional): Numero de puntos con los que se define el hiperplano (numero minimo de
                           puntos para poder hacer un ajuste). Defaults to 3.
        prob (float, optional): Proabilidad de que el subset de puntos no tenga outliers. Defaults to 0.99.
        threshold (float, optional): Punto a partir del cual un punto no se considera que esta bien ajustado por el hiperplano.
                                     Se le da un valor de None para que se calcule el valor automatico. Defaults to None.
        max_iter (int, optional): Iteraciones maximas. Defaults to 15000.

    Returns:
        np.ndarray, np.ndarray: Devuelve las posiciones de los puntos que se consideran inliers y los coeficientes definitivos

    """

    if not threshold:
        threshold = np.median(np.abs(data[:, -1] - np.median(data[:, -1])))
    # Solo se van a comentar las diferencias con la funcion original
    # Los datos ahora ya se pasan con la columna de 1s. Mantenemos A para hacer que la nomenclatura sea la misma
    A = data
    k = max_iter
    support = 1
    iters = 0
    data_size = len(data)
    def_coefs = None

    while iters < k:
        points_ind = np.random.choice(data_size, m, replace=False)
        points = A[points_ind]
        # Se calcula el hiperplano con producto vectorial en vez de svd (numba no lo ejecuta bien con svd)
        vectors = points[1:][:, 1:] - points[0][1:]

        if m > 2:
            normal_vector = np.cross(vectors[0], vectors[1])
        else:
            normal_vector = np.array([-1 * vectors[0][1], vectors[0][0]])

        normal_vector /= np.linalg.norm(normal_vector)

        bias = -np.dot(normal_vector, points[0][1:])

        coefs = np.array([bias] + list(normal_vector))

        support_aux = 0
        for i in A[:, :-1].dot((coefs[:-1] / (-1 * coefs[-1]))) - A[:, -1]:
            if abs(i) < threshold:
                support_aux += 1
        support_aux -= m
        if support_aux > support:
            support = support_aux
            def_coefs = coefs
            k = np.log(1 - prob) / np.log(1 - (support / data_size) ** m)
        iters += 1
    if def_coefs[-1] < 0:
        def_coefs = -1 * def_coefs
    return (
        np.where(
            np.abs(A[:, :-1].dot(def_coefs[:-1] / (-1 * def_coefs[-1])) - A[:, -1])
            < threshold
        ),
        def_coefs,
    )


def sk_ransac(data):
    X = data[:, :-1]
    y = data[:, -1]
    ransac = linear_model.RANSACRegressor()
    ransac.fit(X, y)

    inlier_mask = ransac.inlier_mask_
    # outlier_mask = np.logical_not(inlier_mask)
    coefs = np.array([ransac.estimator_.intercept_, *ransac.estimator_.coef_, -1])
    coefs = -1 * coefs
    return inlier_mask, coefs / np.linalg.norm(coefs)


if __name__ == "__main__":
    # Modulo de pruebas
    # Se crea un dataset y se ejecuta 1000 veces con cada funcion
    # Numba tarda en compilar por lo que la primera ejecucion es mas lenta
    # pero las siguientes son mas rapidas
    n_samples = 1000
    n_outliers = 50

    X, y, coef = datasets.make_regression(
        n_samples=n_samples,
        n_features=1,
        n_informative=1,
        noise=10,
        coef=True,
        random_state=0,
    )
    y = y + 50
    # Add outlier data
    np.random.seed(0)
    X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
    y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
    data = np.array(list(zip([i[0] for i in X], y)))
    A = np.c_[np.ones(data.shape[0]), data]
    execution_time = timeit.timeit(
        lambda: ransac(
            data,
            m=2,
        ),
        globals=globals(),
        number=1000,
    )
    print(f"Execution time base: {execution_time} seconds")

    execution_time = timeit.timeit(
        lambda: sk_ransac(data),
        globals=globals(),
        number=1000,
    )

    print(f"Execution time sklearn: {execution_time} seconds")

    execution_time = timeit.timeit(
        lambda: ransac2(
            A,
            m=2,
        ),
        globals=globals(),
        number=1,
    )

    print(f"Execution time numba 1º: {execution_time} seconds")
    execution_time = timeit.timeit(
        lambda: ransac2(A, m=2), globals=globals(), number=1000
    )
    print(f"Execution time numba x1000: {execution_time} seconds")
    positions, coefs = ransac(data, m=2)
    print(coefs)

    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], color="blue", label="Normal Points")
    plt.scatter(
        data[positions][:, 0],
        data[positions][:, 1],
        color="red",
        label="Highlighted Points",
    )

    # Add labels, legend, and title
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.title("Scatterplot with Highlighted Points")
    plt.show()
