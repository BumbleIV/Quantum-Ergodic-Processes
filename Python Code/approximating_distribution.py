import numpy as np
import matplotlib.pyplot as plt
import math


def rand_sphere_uniform():
    phi = np.random.uniform(0, 2*np.pi)
    z = np.random.uniform(-1, 1)
    r = np.sqrt(1-z**2)
    return (r*np.cos(phi), r*np.sin(phi), z)


def rand_ball_uniform():
    a = rand_sphere_uniform()
    t = np.random.uniform(0, 1)
    r = t**(1/2)
    return (r*a[0], r*a[1], r*a[2])


def rand_sphere_theta(theta):
    z = np.cos(theta)
    r = np.sin(theta)
    phi = np.random.uniform(0, 2*np.pi)
    return(r*np.cos(phi), r*np.sin(phi), z)


def iterate(v, w, g):
    a = np.sqrt(1-g)
    c = np.dot(v, w)
    return [a*v[j]+(g + (a**2 - a)*c)*w[j] for j in range(3)]


def n_times(sphere, ball, n, g):
    v = ball()
    for i in range(n):
        v = iterate(v, sphere(), g)

    return v


def dist(): return rand_sphere_theta(np.pi/4)


def main():
    num = 100
    tries = 100000
    start = rand_ball_uniform()
    gamma = 0.6

    norms = [np.linalg.norm(n_times(dist, start, num, gamma))
             for i in range(tries)]

    plt.hist(norms, 70, (0, 1))
    plt.show()
