# random azimuthal angle at each step
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import random

l = 0.01
d = math.pi/12
N = 1000
v0 = [1, 0, 0]
theta = math.pi/2
omega = 0.1

phi = 0
v = np.zeros((3, N+1))
v[:, 0] = v0


for j in range(N):
    phi = 2*math.pi*random.random()
    u = [np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)]
    w = [l*u[k] + (1-l)*(np.dot(u, v[:, j]))*u[k]+np.sqrt(1-l)*(np.cos(d)*(v[k, j] -
                                                                           np.dot(u, v[:, j])*u[k])+np.sin(d)*np.cross(v[:, j], u)[k]) for k in range(3)]
    v[:, j+1] = w


a = np.linspace(0, 2 * np.pi, 100)
b = np.linspace(0, np.pi, 100)

x = 1 * np.outer(np.cos(a), np.sin(b))
y = 1 * np.outer(np.sin(a), np.sin(b))
z = 1 * np.outer(np.ones(np.size(a)), np.cos(b))

norm = [np.sqrt(np.dot(v[:, j], v[:, j])) for j in range(N+1)]
colors = [[np.sqrt(0.3*(1-norm[j])), np.sqrt(0.6*(1-norm[j])),
           np.sqrt(0.9*(1-norm[j]))] for j in range(N+1)]

fig = plt.figure(figsize=plt.figaspect(0.77)*1.5)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(v[0], v[1], v[2], c=colors, linestyle='dashed', linewidth=2)
[ax.plot([v[0, j], v[0, j+1]], [v[1, j], v[1, j+1]],
         [v[2, j], v[2, j+1]], color=colors[j]) for j in range(N)]
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color=[
                0.7, 0.7, 0.84], linewidth=0, alpha=0.1)


plt.show()
