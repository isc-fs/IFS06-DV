from ransac import ransac, sk_ransac, ransac2
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import timeit
from rotaciones import vectors2matrix


def benchmark(func, data):
    for ts_data in data:
        if func.__name__ == "ransac2":
            ts_data = np.c_[np.ones(ts_data.shape[0]), ts_data]
        func(ts_data)


def performance_test(path):
    data = read_lidar_data(path)
    execution_time = timeit.timeit(
        lambda: benchmark(sk_ransac, data),
        globals=globals(),
        number=1,
    )

    print(f"Execution time sklearn: {execution_time} seconds")
    execution_time = timeit.timeit(
        lambda: benchmark(ransac, data),
        globals=globals(),
        number=1,
    )

    print(f"Execution time normal: {execution_time} seconds")

    execution_time = timeit.timeit(
        lambda: benchmark(ransac2, data),
        globals=globals(),
        number=1,
    )

    print(f"Execution time numba: {execution_time} seconds")

    execution_time = timeit.timeit(
        lambda: benchmark(ransac2, data),
        globals=globals(),
        number=1,
    )

    print(f"Execution time numba (after 1st iter): {execution_time} seconds")


def ground_removal(path):
    data = read_lidar_data(path)
    k = np.zeros(data[0].shape[1])
    k[-1] = 1
    for ts_data in data:

        inliers, def_coefs = ransac(ts_data, prob=0.9999)
        pass
        ts_data1 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data1, inliers)
        inliers_sk, def_coefs = sk_ransac(ts_data)
        pass
        ts_data2 = ts_data @ vectors2matrix(
            k, def_coefs[1:] / np.linalg.norm(def_coefs[1:])
        )
        plot_3d_points(ts_data2, inliers_sk)
        inliers, def_coefs = ransac2(
            np.c_[np.ones(ts_data.shape[0]), ts_data], prob=0.9999
        )
        pass
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
    # plt.axis("equal")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.legend()
    plt.title("Scatterplot with Highlighted Points")
    plt.show()


if __name__ == "__main__":
    ground_removal("puntos_lidar.txt")
    # performance_test("puntos_lidar.txt")
