# Next Goal: make the Bloch sphere a superclass.
# Make it possible to create a Bloch sphere with different parameters.


import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def Bloch(lambd=0.01, delta=math.pi/12, N=10000, v0=[1, 0, 0], theta=math.pi/2, omega=1.1, phi=0):
    """ 
    This function creates the Bloch sphere based on user input. Default parameters are provided.
    Lambda is named "lambd" to avoid confusion with the lambda function in Python.
    COMPLETE
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

    return v


def Plot(v, N=10000):
    """
    This function 3D-plots the Bloch sphere.
    COMPLETE
    """

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
    """
    Ask user for input and plot the Bloch sphere. 
    If no input is given, default parameters are used
    INCOMPLETE
    """

    while True:
        print("Press Enter button to use default parameters.")
        print("Press 'P' or 'p' to plot the Bloch sphere.")

        user_input = input("\n")

        if user_input == "":
            v = Bloch()
            Plot(v)
            break

        elif user_input.upper() == "P":
            pass

    v = Bloch(lambd, delta, N, v0, theta, omega, phi)
    Plot(v, N)


if __name__ == "__main__":
    main()


# #############################################################################
# take spherically symmetric function and vary gamma. "histogrammify" it.
# find list of points.
#
# what happens with the density of points? what is the distribution of points?
# also vary theta.
