# import modules containing features not already in the standard library
import math
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    """

    # lamb = input("Lambda: ")
    # lamb = float(lamb)

    # delta = input("Delta: ")
    # delta = float(math.pi/float(delta))

    # N = input("N: ")
    # N = int(N)

    # vector_0 = np.array([1, 0, 0])

    # phi = 0

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    z_line = np.linspace(0, 15, 1000)
    x_line = np.cos(z_line)
    y_line = np.sin(z_line)
    ax.plot3D(x_line, y_line, z_line, 'gray')

    z_points = 15 * np.random.random(100)
    x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
    y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
    ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv')

    plt.show()


if __name__ == '__main__':
    main()
