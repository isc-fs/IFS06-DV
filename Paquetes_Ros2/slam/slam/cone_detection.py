"""
========================
cone_detection.py (v1.0)
========================

Elaborado por Sergio Jiménez para el ISC
Permite detectar las posiciones de los conos dados los
datos de un LIDAR. Este archivo tiene distintos benchmarks, 
ademas de permitir visualizar la comparacion entre lo predicho 
y los datos
"""

from slam.ransac import ransac, ransac2
from slam.ground_removal import cone_fit, read_lidar_data, clustering_separation
from slam.rotaciones import vectors2matrix
import numpy as np
from sklearn.cluster import DBSCAN
import cProfile
import time
import matplotlib.pyplot as plt
import timeit


def final_cone_result_rt(data, model=DBSCAN):
    """
    Permite sacar los conos a partir de los datos del lidar. Version
    para Real Time. Aplica RANSAC, Clustering y el ajuste de cono. Esta hecha
    para solo hacer una medida del lidar de una vez

    Args:
        data (np.ndarray): los datos del lidar
        model (sklearn.model, optional): modelo de clustering empleado. Sirve una implementacion
                                         propia si es una clase con metodo fit_transform. Defaults to DBSCAN.

    Returns:
        float, float: las posiciones x e y de la punta del cono (a y b de los parametros del cono)
    """

    labels, clean_data, def_coefs = clustering_separation_rt(data, model)
    separated_data = [
        np.array(clean_data[labels == label]) for label in np.unique(labels)
    ]
    cone_positions = []
    for cone in separated_data:

        if len(cone) > 3:
            v = np.array([0, 0, -1 * def_coefs[0]])
            w = np.array(def_coefs[1:])
            lidar_distance_to_floor = np.dot(v, w) / np.linalg.norm(w)
            # cone_positions.append((np.mean(cone[:, 0]), np.mean(cone[:, 1])))
            clean_cone = cone[cone[:, 2] > 0.04 + lidar_distance_to_floor]
            ### ATENCION: el solver es SLSQP porque en los benchmarks es el que es el mas rapido
            # L-BFGS-P tambien era bastante rapido, pero no he comparado rendimiento entre ellos
            params = cone_fit(clean_cone, solver="SLSQP")
            if params[2] < 6 and params[2] > 5 and params[3] < 0.4 and params[3] > 0.3:
                cone_positions.append((params[0], params[1]))
    return cone_positions


def clustering_separation_rt(data, model):
    """
    Realiza la separación en clusters mediante un modelo de clustering. Primero hace ransac
    (se podría cambiar por cualquiera de las otras implementaciones), deshace las posibles rotaciones
    de los datos por el movimiento del coche y despues hace el clustering. Pensada para RT

    Args:
        data (str): ruta a los datos
        model (sklearn_model): el modelo de clustering de sklearn. Podría usarse una implementación propia si
                               se implementa como una clase con un metodo fit_predict que hace el ajuste y devuelve
                               las predicciones


    Returns:
        np.ndarray, np.ndarray, np.ndarray: las etiquetas para saber a que cluster pertenece cada cono,
                                            los datos con la correccion de rotacion y los coeficientes
                                            del plano sacado por ransac
    """
    A = np.c_[np.ones(data.shape[0]), data]
    inliers, def_coefs = ransac2(A, prob=0.9999)
    # COrreccion de rotacion (transformamos el vector normal al plano en un vector vertical, solo componente z)
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

    return labels, data, def_coefs


def profiling_cone_detection():
    """
    Hace profiling a la funcion de sacar los conos para saber que funciones
    son las que tardan mas
    """
    cProfile.run("benchmark_cone_detection(data)")


def solvers_benchmark(data, solver, model=DBSCAN):
    """
    Hace el benchmark para 1 solver en concreto

    Args:
        data (np.ndarray): los datos
        solver (str): el solver que se debe usar
        model (sklearn.model, optional): Modelo de clustering. Defaults to DBSCAN.
    """
    labels, clean_data, def_coefs = clustering_separation_rt(data, model)
    separated_data = [
        np.array(clean_data[labels == label]) for label in np.unique(labels)
    ]
    for cone in separated_data:

        if len(cone) > 3:
            v = np.array([0, 0, -1 * def_coefs[0]])
            w = np.array(def_coefs[1:])
            lidar_distance_to_floor = np.dot(v, w) / np.linalg.norm(w)
            # cone_positions.append((np.mean(cone[:, 0]), np.mean(cone[:, 1])))
            clean_cone = cone[cone[:, 2] > 0.05 + lidar_distance_to_floor]
            if len(clean_cone) > 3:
                cone_fit(clean_cone, solver)


def best_solver(data):
    """
    Para benchmarkear los solvers de scipy.minimize

    Args:
        data (np.ndarray): los datos
    """
    solvers = [
        "Nelder-Mead",
        "Powell",
        "CG",
        "BFGS",
        # "Newton-CG",
        "L-BFGS-B",
        "TNC",
        "COBYLA",
        "SLSQP",
        # "dogleg",
        "trust-constr",
        # "trust-ncg",
        # "trust-exact",
        # "trust-krylov",
    ]
    for solver in solvers:
        execution_time = timeit.timeit(
            lambda: solvers_benchmark(data, solver),
            globals=globals(),
            number=1,
        )

        print(f"Execution time {solver}: {execution_time} seconds")


def benchmark_cone_detection(data):
    """
    Ejecuta el cone detection en todos los datos

    Args:
        data (np.ndarray): los datos
    """
    for d in data:
        final_cone_result_rt(d)


def benchmark_process(data):
    """
    Calcula cuanto tiempo se tarda en todo el dataset

    Args:
        data (np.ndarray): los datos
    """
    execution_time = timeit.timeit(
        lambda: benchmark_cone_detection(data),
        globals=globals(),
        number=1,
    )

    print(f"Execution time: {execution_time} seconds")
    print(f"{len(data)} data points")
    print(f"{execution_time/len(data)} mean time")
    print(f"{len(data)/execution_time} mean fps")


def compare_data_to_processed(data):
    """
    Permite ver (en 2D) las posiciones predichas para los conos
    y los clusters separados por el lidar para unos datos concretos

    Args:
        data (np.ndarray): los datos
    """
    for d in data:
        x, y = zip(*final_cone_result_rt(d))
        plt.scatter(x, y, marker="*")
        clustering_separation(d, plot=True)


if __name__ == "__main__":
    data = read_lidar_data("puntos_lidar.txt")

    final_cone_result_rt(data[0])
    profiling_cone_detection()
    benchmark_process(data)
    # compare_data_to_processed(data)

    # best_solver(data)
