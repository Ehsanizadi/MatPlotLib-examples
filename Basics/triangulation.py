from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

x = [1,0,1,0,1,0,1,0.5]
y = [0,1,1,0,0,1,1,0.5]
z = [0,0,0,1,1,1,1,3]

x1 = [5,6,5,6,5,6,5,6,5.5]
y1 = [5,5,6,6,5,5,6,6,5.5]
z1 = [5,5,5,5,6,6,6,6,3]



fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
ax.plot_trisurf(x1, y1, z1, linewidth=0.6)

plt.show()


