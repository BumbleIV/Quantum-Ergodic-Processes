#rotation of the damping direction for two starting states
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D

l = 0.01
d = math.pi/12
N=10000
v0 = [0.7,0,0]
w0 = [0,0.7,0]
theta = math.pi/3
omega = 0.1

phi = 0
v = np.zeros((3, N+1))
v[:,0]=v0
w = np.zeros((3, N+1))
w[:,0]=w0

for j in range(N):
    u = [np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)]
    phi = phi + omega
    p = [l*u[k] + (1-l)*(np.dot(u,v[:,j]))*u[k]+np.sqrt(1-l)*(np.cos(d)*(v[k,j]-np.dot(u,v[:,j])*u[k])+np.sin(d)*np.cross(v[:,j],u)[k]) for k in range(3)]
    v[:,j+1] = p
    
for j in range(N):
    u = [np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)]
    phi = phi + omega
    p = [l*u[k] + (1-l)*(np.dot(u,w[:,j]))*u[k]+np.sqrt(1-l)*(np.cos(d)*(w[k,j]-np.dot(u,w[:,j])*u[k])+np.sin(d)*np.cross(w[:,j],u)[k]) for k in range(3)]
    w[:,j+1] = p
    
    
    
a = np.linspace(0, 2 * np.pi, 100)
b = np.linspace(0, np.pi, 100)

x = 1 * np.outer(np.cos(a), np.sin(b))
y = 1 * np.outer(np.sin(a), np.sin(b))
z = 1 * np.outer(np.ones(np.size(a)), np.cos(b))
    
norm = [np.sqrt(np.dot(v[:,j],v[:,j])) for j in range(N+1)]
colors1 = [[np.sqrt(0.3*(1-norm[j])), np.sqrt(0.6*(1-norm[j])), np.sqrt(0.9*(1-norm[j]))] for j in range(N+1)]
colors2 = [[np.sqrt(0.9*(1-norm[j])), np.sqrt(0.6*(1-norm[j])), np.sqrt(0.3*(1-norm[j]))] for j in range(N+1)]


fig = plt.figure(figsize=plt.figaspect(0.77)*1.5)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(v[0],v[1],v[2], c=colors1)
ax.scatter(w[0],w[1],w[2], c=colors2)
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color=[0.7,0.7,0.84], linewidth=0, alpha=0.1)







