import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def Bloch(lambd=0.01, delta=math.pi/12, N=100000, v0=[1, 0, 0], theta=math.pi/2, omega=1.1, phi=0):
    """ 
    This function forms the Bloch sphere with default parameters. 
    Lambda is named "lambd" to avoid confusion with the lambda function in Python.
    """

    v = np.zeros((3, N+1))
    v[:, 0] = v0

    for i in range(N):
        u = [np.sin(theta) * np.cos(phi), np.sin(theta)
             * np.sin(phi), np.cos(theta)]

        phi += omega

        w = [lambd * u[k] + (1-lambd) * (np.dot(u, v[:, i])) * u[k] + np.sqrt(1-lambd) * (np.cos(delta) * (
            v[k, i] - np.dot(u, v[:, i]) * u[k]) + np.sin(delta) * np.cross(v[:, i], u)[k]) for k in range(3)]

        v[:, i + 1] = w

    a = np.linspace(0, 2 * np.pi, 100)
    b = np.linspace(0, np.pi, 100)

    x = 1 * np.outer(np.cos(a), np.sin(b))
    y = 1 * np.outer(np.sin(a), np.sin(b))
    z = 1 * np.outer(np.ones(np.size(a)), np.cos(b))

    norm = [np.sqrt(np.dot(v[:, j], v[:, j])) for j in range(N + 1)]

    colors = [[np.sqrt(0.3 * (1 - norm[j])), np.sqrt(0.6 * (1 - norm[j])),
               np.sqrt(0.9 * (1 - norm[j]))] for j in range(N + 1)]

    fig = plt.figure(figsize=plt.figaspect(0.77) * 1.5)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(v[0], v[1], v[2], c=colors)
    ax.plot_surface(x, y, z,  rstride=4, cstride=4, color=[
                    0.7, 0.7, 0.84], linewidth=0, alpha=0.1)

    plt.show()


def main():
    Bloch()


if __name__ == "__main__":
    main()
