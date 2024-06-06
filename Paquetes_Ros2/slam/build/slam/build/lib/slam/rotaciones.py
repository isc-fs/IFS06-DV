"""
====================
rotaciones.py (v1.0)
====================

Elaborada por Sergio Jimenez Romero para el ISC
Permite obtener matrices de rotacion a partir de un vector
y su rotacion 
"""

import numpy as np
from scipy.spatial.transform import Rotation as R


def vectors2matrix(v1, v2):
    """
    Dado un vector y su version rotada halla la matriz de la
    rotacion y la devuelve. Los vectores tienen que estar normalizados

    Args:
        v1 (np.ndarray): el primer vector
        v2 (np.ndarray): el segundo vector

    Returns:
        np.ndarray: la matriz de rotacion
    """
    v_rot = np.cross(v1, v2)
    angle = np.arccos(np.dot(v1, v2))
    v_norm = np.linalg.norm(v_rot)
    if v_norm == 0:
        if angle == 0:
            return np.eye(v1.shape[0])
        else:
            return -1 * np.eye(v1.shape[0])
    else:
        v_rot /= v_norm
        rotation = R.from_rotvec(v_rot * angle)
        return rotation.as_matrix()


if __name__ == "__main__":
    v1 = np.array([1, 0, 0])
    v2 = np.array([-1, 0, 0])
    v3 = np.array([np.cos(np.pi / 4), np.sin(np.pi / 4), 0])
    print(vectors2matrix(v1, v1))
    print(vectors2matrix(v1, v2))
    print(vectors2matrix(v1, v3))
