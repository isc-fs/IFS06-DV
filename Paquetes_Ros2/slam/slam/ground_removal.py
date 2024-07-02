"""
========================
ground_removal.py (v1.1)
========================

Elaborado por Sergio Jimenez para el ISC
Contiene varias funciones utilizadas en el proceso de percepcion,
más específicamente para la percepción con LIDAR. Es posible que 
en un futuro este archivo se separe en varios archivos

Incluye funciones para:
- Evaluar el rendimiento de las implementaciones de RANSAC


Cambios v1.1:
- Inclusion de numba en algunas funciones
- Cambios menores por compatinilidad con cone_detection
"""

from slam.ransac import ransac, sk_ransac, ransac2
import matplotlib.pyplot as plt
import numpy as np
import timeit
from slam.rotaciones import vectors2matrix
from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering,
    DBSCAN,
    Birch,
    BisectingKMeans,
)
from sklearn.mixture import GaussianMixture
from scipy.optimize import minimize, least_squares
import numba


# No todos los modelos se usan, estan para hacer el benchmarking
modelos = [
    KMeans,
    # SpectralClustering,
    AgglomerativeClustering,
    DBSCAN,
    # OPTICS,
    Birch,
    BisectingKMeans,
    GaussianMixture,
]


def benchmark(func, data):
    """
    Esta funcion sirve para evaluar el rendimiento de las implementaciones
    de ransac en un dataset que viene en la variable data (en principio puntos_lidar.txt)

    Args:
        func (func): la implementacion de ransac
        data (np.ndarray): el array de numpy con los datos
    """
    for ts_data in data:
        if func.__name__ == "ransac2":
            # Si es ransac2 añadimos la columna del sesgo porque numba no deja
            # añadirla en la propia funcion (que yo sepa)
            ts_data = np.c_[np.ones(ts_data.shape[0]), ts_data]
        func(ts_data)


def performance_test(path):
    """
    Funcion que sirve para evaluar todas las implementaciones de
    RANSAC juntas. Carga los datos y cronometra la ejecucion

    Args:
        path (str): la ruta al fichero con los datos
    """
    data = read_lidar_data(path)
    models = {
        "sklearn": sk_ransac,
        "normal": ransac,
        "numba (1º iter)": ransac2,
        "numba": ransac2,
    }
    for model_name, model in models.items():
        execution_time = timeit.timeit(
            lambda: benchmark(model, data),
            globals=globals(),
            number=1,
        )

        print(f"Execution time {model_name}: {execution_time} seconds")


def clustering(path, model, plot=False, threeD=False):
    """
    Funcion que permite realizar el clustering para cada
    instante de tiempo dado un modelo de clustering y la
    ruta a los datos

    Args:
        path (str): ruta a los datos
        model (sklearn_model): el modelo de clustering de sklearn. Podría usarse una implementación propia si
                               se implementa como una clase con un metodo fit_predict que hace el ajuste y devuelve
                               las predicciones
        plot (bool, optional): Si se deben representar los datos. Defaults to False.
        threeD (bool, optional): Si la representacion de los datos debe ser 3D. Defaults to False.
    """
    data = read_lidar_data(path)
    for ts_data in data:
        clustering_separation(ts_data, model, plot, threeD)


def clustering_separation(data, model=DBSCAN, plot=False, threeD=False):
    """
    Realiza la separación en clusters mediante un modelo de clustering. Primero hace ransac
    (se podría cambiar por cualquiera de las otras implementaciones), deshace las posibles rotaciones
    de los datos por el movimiento del coche y despues hace el clustering. Si se indica, representa los
    datos (en 2D/3D)

    Args:
        data (np.ndarray): los datos
        model (sklearn_model): el modelo de clustering de sklearn. Podría usarse una implementación propia si
                               se implementa como una clase con un metodo fit_predict que hace el ajuste y devuelve
                               las predicciones
        plot (bool, optional): Si se deben representar los datos. Defaults to False.
        threeD (bool, optional): Si la representacion de los datos debe ser 3D. Defaults to False.

    Returns:
        np.ndarray, np.ndarray, np.ndarray: las etiquetas para saber a que cluster pertenece cada cono,
                                            los datos con la correccion de rotacion y los coeficientes
                                            del plano sacado por ransac
    """
    inliers, def_coefs = ransac(data, prob=0.9999)
    # Correccion de rotacion (transformamos el vector normal al plano en un vector vertical, solo componente z)
    k = np.zeros(data.shape[1])
    k[-1] = 1

    outliers = np.ones(data.shape[0], dtype=bool)
    outliers[inliers] = False
    data = (data @ vectors2matrix(k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])))[
        outliers
    ]
    # OTRAS OPCIONES DE MODELOS (por ahora he puesto DBSCAN)
    # clust_model = model()
    # clust_model = AgglomerativeClustering(
    #     n_clusters=None,
    #     linkage="ward",
    #     compute_full_tree=True,
    #     distance_threshold=0.5,
    # )
    clust_model = DBSCAN(eps=0.3, min_samples=2)
    labels = clust_model.fit_predict(data)
    if plot:
        colors = plt.cm.nipy_spectral(labels.astype(float) / len(set(labels)))

        if not threeD:
            plt.scatter(
                data[:, 0],
                data[:, 1],
                marker=".",
                s=30,
                lw=0,
                alpha=0.7,
                c=colors,
                edgecolor="k",
            )
        else:
            fig = plt.figure()

            ax = fig.add_subplot(projection="3d")
            ax.scatter(
                data[:, 0],
                data[:, 1],
                data[:, 2],
                marker=".",
                s=30,
                lw=0,
                alpha=0.7,
                c=colors,
                edgecolor="k",
            )
            plt.axis("equal")
        plt.title(f"Modelo: {model.__name__}")
        plt.show()
    return labels, data, def_coefs


@numba.njit
def cone_model(params, x, y):
    """
    Formula del cono empleada en la implementacion del ajuste del
    cono. Sirve para que scipy.minimize sepa cual es la formula del cono

    Args:
        params (list): la lista de los parametros
        x (np.ndarray): lass posiciones x de los datos
        y (np.ndarray): las posiciones y de los datos

    Returns:
        np.ndarray: la posicion z de los puntos
    """
    a, b, c, d = params
    # Formula generalizada de un cono
    return d - c * np.sqrt((x - a) ** 2 + (y - b) ** 2)


@numba.njit
def objective_function(params, x, y, z):
    """
    Funcion a minimizar por minimize. Para el ajuste de
    un cono buscamos que su error cuadratico medio sea lo
    mas pequeño posible

    Args:
        params (list): lista de los parametros del cono
        x (np.ndarray): los valores de las x de los puntos
        y (np.ndarray): los valores de las y de los puntos
        z (np.ndarray): Los valores de las z de los puntos

    Returns:
        float: el error cuadratico medio
    """
    z_pred = cone_model(params, x, y)
    return np.mean((z - z_pred) ** 2)


def residuals(params, x, y, z):
    return z - cone_model(params, x, y)


def ls_cone_fit(data):
    """
    Realiza el ajuste de un cono a los datos
    minimizando el error cuadratico medio, con leastsq
    en vez de minimize

    Args:
        data (np.ndarray): los datos

    Returns:
        float, float, float, float: Los parametros del cono
    """
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]

    # Estos son los parametros con los que empieza
    # (estan puestos asi porque no estan muy lejos de los valores reales)
    a = np.mean(x)
    b = np.mean(y)
    c = 5.5
    d = 0.35

    result = least_squares(residuals, [a, b, c, d], args=(x, y, z))

    a, b, c, d = result.x

    return a, b, c, d


def cone_fit(data, solver="L-BFGS-B"):
    """
    Realiza el ajuste de un cono a los datos
    minimizando el error cuadratico medio

    Args:
        data (np.ndarray): los datos

    Returns:
        float, float, float, float: Los parametros del cono
    """
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, 2]

    # Estos son los parametros con los que empieza
    # (estan puestos asi porque no estan muy lejos de los valores reales)
    a = np.mean(x)
    b = np.mean(y)
    c = 5.5
    d = 0.35

    result = minimize(objective_function, [a, b, c, d], args=(x, y, z), method=solver)

    a, b, c, d = result.x

    return a, b, c, d


def plot_cone_vs_data(cone_params, data, fig=None):
    """
    Crea un grafico en el que se muestra el cono estimado y los puntos del lidar


    Args:
        cone_params (list): los parametros del cono (a,b,c,d)
        data (np.ndarray): Los datos del lidar
        fig (plt.figure, optional): Grafico al que plotear (para poder acumular
                                    varios conos en la misma grafica). Defaults to None.
    """
    plot = False
    a, b, c, d = cone_params
    x, y, z = generate_cone_plot_points(a, b, c, d)
    if not fig:
        fig = plt.figure()
        plot = True
    ax = fig.add_subplot(projection="3d")
    cone_val = d - c * np.sqrt(((data[:, 0] - a) ** 2 + (data[:, 1] - b) ** 2))
    ax.scatter(
        x,
        y,
        z,
        color="red",
        label="Conos",
    )
    ax.scatter(
        data[:, 0],
        data[:, 1],
        cone_val,
        color="green",
        label="Pred",
    )
    ax.scatter(
        data[:, 0],
        data[:, 1],
        data[:, 2],
        color="blue",
        label="Puntos",
    )
    # OTROS GRAFICOS EN COORDENADAS CILINDRICAS Y ESFERICAS
    # ax.scatter(
    #     x**2 + y**2,
    #     y / x,
    #     z,
    #     color="black",
    #     label="Puntos",
    # )
    # ax.scatter(
    #     np.sqrt(x**2 + y**2 + z**2),
    #     y / x,
    #     np.arccos(z) / np.sqrt(x**2 + y**2 + z**2),
    #     color="black",
    #     label="Puntos",
    # )
    # ax.scatter(
    #     x,
    #     y,
    #     np.log(np.sqrt(x**2 + y**2)),
    #     color="red",
    #     label="Conos",
    # )
    if plot:
        plt.show()


def generate_cone_plot_points(a, b, c, d, num_slices=50):
    """
    Genera los puntos para dibujar el cono

    Args:
        a (float): posicion x de la punta del cono
        b (float): posicion y de la punta del cono
        c (float): como de ancho/estrecho es el cono
        d (float): altura a la que se encuntra el cono
        num_slices (int, optional): numero de puntos para generar el cono tanto para
                                    cuantos son verticalmente como horizontalmente. Defaults to 50.

    Returns:
        float, float, float: los puntos del cono
    """
    # Create the data for the cone
    theta = np.linspace(0, 2 * np.pi, num_slices)
    z = np.linspace(-0.1, d, num_slices)
    r = d / c
    theta, z = np.meshgrid(theta, z)
    print(r, a, b, c, d)
    x = (r * (d - z) / d * np.cos(theta)) + a
    y = (r * (d - z) / d * np.sin(theta)) + b
    return x, y, z


def final_cone_result_file(path, model=DBSCAN):
    """
    Permite sacar los conos a partir de los datos del lidar. Esta version no es para
    Real Time, es para datos recopilados (lee de un fichero y plotea). Aplica RANSAC
    hace clustering y ajusta los conos para sacar las posiciones de estos

    Args:
        path (str): ruta a los datos
        model (sklearn.model, optional): modelo de clustering empleado. Sirve una implementacion
                                         propia si es una clase con metodo fit_transform. Defaults to DBSCAN.
    """
    data = read_lidar_data(path)
    for ts_data in data:
        labels, clean_data, def_coefs = clustering_separation(ts_data, model)
        separated_data = [
            np.array(clean_data[labels == label]) for label in np.unique(labels)
        ]
        for cone in separated_data:
            if len(cone) > 3:

                # print(cone[cone[:, -1] > -0.05][:, -1])
                params = cone_fit(cone[cone[:, -1] > -0.05])
                # print(params)
                plot_cone_vs_data(params, cone)  # [cone[:, -1] > -0.05])


def clustering_benchmark(path):
    """
    Permite hacer un benchmark a los distintos modelos de clustering. Tener en
    cuenta que el tiempo tambien incluye lectura de los datos

    Args:
        path (str): ruta al fichero con los datos
    """
    for model in modelos:
        print(model)
        execution_time = timeit.timeit(
            lambda: clustering(path, model),
            globals=globals(),
            number=1,
        )

        print(f"Execution time {model.__name__}: {execution_time} seconds")


def plot_clustering(path):
    """
    Hace el clustering para cada modelo. Hace todos los frames para cada modelo, por lo que
    no es muy util para comparar si el dataset es muy largo. Se recomienda usar unas 5 muestras

    Args:
        path (str): ruta al fichero
    """
    for model in modelos:
        clustering(path, model, plot=True, threeD=True)


def ground_removal(path):
    """
    Compara el RANSAC aplicado a ground removal de las 3 implementaciones de
    ransac.py

    Args:
        path (str): la ruta al fichero de los datos
    """
    data = read_lidar_data(path)
    # Para corregir la rotacion
    k = np.zeros(data[0].shape[1])
    k[-1] = 1
    for ts_data in data:
        # Version normal
        inliers, def_coefs = ransac(ts_data, prob=0.9999)
        # Correccion rotacion
        ts_data1 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        # plot
        plot_3d_points(ts_data1, inliers)
        # Version sklearn
        inliers_sk, def_coefs = sk_ransac(ts_data)
        ts_data2 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data2, inliers_sk)
        # Version numba
        inliers, def_coefs = ransac2(
            np.c_[np.ones(ts_data.shape[0]), ts_data], prob=0.9999
        )
        ts_data3 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data3, inliers)


def read_lidar_data(path):
    """
    Carga los datos del lidar de un txt. Los datos de distintos
    instantes de tiempo tienen que estar separados por tres guiones
    (---) para que se separen

    Args:
        path (str): ruta al fichero con los datos

    Returns:
        list: lista con los arrays de datos
    """
    with open(path, "r") as file:
        data = file.read()

    # Split the content by the custom delimiter
    array_strings = data.strip().lstrip("---").split(f"\n---\n")

    # Convert each part back into a NumPy array
    arrays = [np.loadtxt(arr.splitlines(), delimiter=",") for arr in array_strings]

    return arrays


def plot_3d_points(data, inliers):
    """
    Representa los puntos de RANSAC en 3D, separando
    inliers de outliers

    Args:
        data (np.ndarray): los datos
        inliers (np.ndarray): cuales son inliers de los datos
    """
    outliers = np.ones(data.shape[0], dtype=bool)
    outliers[inliers] = False

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(
        data[outliers][:, 0],
        data[outliers][:, 1],
        data[outliers][:, 2],
        color="red",
        label="Conos",
    )
    ax.scatter(
        data[inliers][:, 0],
        data[inliers][:, 1],
        data[inliers][:, 2],
        color="blue",
        label="Inliers (suelo)",
    )
    # Para representacion en escala real
    plt.axis("equal")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.title("Scatterplot with Highlighted Points")
    plt.show()


if __name__ == "__main__":
    # Las funciones hacen distintas cosas, consultar la que se necesite
    path = "puntos_lidar.txt"
    # ground_removal(path)
    # performance_test(path)
    # clustering_benchmark(path)
    # plot_clustering(path)
    final_cone_result_file(path)
