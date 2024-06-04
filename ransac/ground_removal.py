from ransac import ransac, sk_ransac, ransac2
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import timeit
from rotaciones import vectors2matrix
from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering,
    DBSCAN,
    Birch,
    BisectingKMeans,
)
from sklearn.mixture import GaussianMixture

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
from scipy.optimize import minimize


def benchmark(func, data):
    for ts_data in data:
        if func.__name__ == "ransac2":
            ts_data = np.c_[np.ones(ts_data.shape[0]), ts_data]
        func(ts_data)


def performance_test(path):
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
    data = read_lidar_data(path)
    for ts_data in data:
        clustering_separation(ts_data, model, plot, threeD)


def clustering_separation(data, model, plot=False, threeD=False):
    inliers, def_coefs = ransac(data, prob=0.9999)
    k = np.zeros(data.shape[1])
    k[-1] = 1

    outliers = np.ones(data.shape[0], dtype=bool)
    outliers[inliers] = False
    data = (data @ vectors2matrix(k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])))[
        outliers
    ]

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


def cone_model(params, x, y):
    a, b, c, d = params
    return d - c * np.sqrt((x - a) ** 2 + (y - b) ** 2)


def objective_function(params, x, y, z):
    z_pred = cone_model(params, x, y)
    return np.mean((z - z_pred) ** 2)


def cone_fit(data):
    x = data[:, 0]
    y = data[:, 1]
    z = data[:, -1]

    a = np.mean(x)
    b = np.mean(y)
    c = 6
    d = 0.225

    result = minimize(objective_function, [a, b, c, d], args=(x, y, z))

    # Extract the optimal parameters
    a, b, c, d = result.x

    return a, b, c, d


def plot_cone_vs_data(cone_params, data, fig=None):
    a, b, c, d = cone_params
    x, y, z = generate_cone_plot_points(a, b, c, d)
    if not fig:
        fig = plt.figure()
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
    # if not fig:
    plt.show()


def generate_cone_plot_points(a, b, c, d, num_slices=50):

    # Create the data for the cone
    theta = np.linspace(0, 2 * np.pi, num_slices)
    z = np.linspace(-0.1, d, num_slices)
    r = d / c
    theta, z = np.meshgrid(theta, z)
    print(r, a, b, c, d)
    x = (r * (d - z) / d * np.cos(theta)) + a
    y = (r * (d - z) / d * np.sin(theta)) + b
    return x, y, z


def final_cone_result(data, model=DBSCAN):
    data = read_lidar_data(path)
    for ts_data in data:
        labels, clean_data, def_coefs = clustering_separation(ts_data, model)
        separated_data = [
            np.array(clean_data[labels == label]) for label in np.unique(labels)
        ]
        for cone in separated_data:
            if len(cone) > 3:
                """
                meter def_coefs para quitar los puntos que esten cerca del suelo
                """
                # print(cone[cone[:, -1] > -0.05][:, -1])
                params = cone_fit(cone[cone[:, -1] > -0.05])
                # print(params)
                plot_cone_vs_data(params, cone)  # [cone[:, -1] > -0.05])

        pass


def clustering_benchmark(path):
    for model in modelos:
        print(model)
        execution_time = timeit.timeit(
            lambda: clustering(path, model),
            globals=globals(),
            number=1,
        )

        print(f"Execution time {model.__name__}: {execution_time} seconds")


def plot_clustering(path):
    for model in modelos:
        clustering(path, model, plot=True, threeD=True)


def ground_removal(path):
    data = read_lidar_data(path)
    k = np.zeros(data[0].shape[1])
    k[-1] = 1
    for ts_data in data:

        inliers, def_coefs = ransac(ts_data, prob=0.9999)
        ts_data1 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data1, inliers)
        inliers_sk, def_coefs = sk_ransac(ts_data)
        ts_data2 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data2, inliers_sk)
        inliers, def_coefs = ransac2(
            np.c_[np.ones(ts_data.shape[0]), ts_data], prob=0.9999
        )
        ts_data3 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data3, inliers)


def read_lidar_data(path):
    with open(path, "r") as file:
        data = file.read()

    # Split the content by the custom delimiter
    array_strings = data.strip().lstrip("---").split(f"\n---\n")

    # Convert each part back into a NumPy array
    arrays = [np.loadtxt(arr.splitlines(), delimiter=",") for arr in array_strings]

    return arrays


def plot_3d_points(data, inliers):
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
    path = "puntos_lidar.txt"
    # ground_removal(path)
    # performance_test(path)
    # clustering_benchmark(path)
    # plot_clustering(path)
    final_cone_result(path)
