# This code, plots the strain of membrane in 2D extended view (cylindrical membrane conveted to rectangule with width of 2(pi)r and height of Z)
from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np


# Initial settings
fig1 = plt.figure(facecolor='white')

x, y, z, deforamtion = np.loadtxt('membraneStrain-initial.csv', delimiter=',', unpack=True, skiprows=1)

membraneRadius = 25.8
Z=z
X=x
# making X of the plot
for i in range(0,len(x)): 
	X[i] =0 + (i%80) *2.026327262


# Making grid
xGrid = np.linspace(0, 162, 80)
yGrid = np.linspace(-10, 105, 80)
# grid the data.
zGrid = griddata(X, z, deforamtion, xGrid, yGrid, interp='linear')


# contour the gridded data, plotting dots at the nonuniform data points.
CS = plt.contour(xGrid, yGrid, zGrid, 10, linewidths=0.1, colors='grey')
CS = plt.contourf(xGrid, yGrid, zGrid, 10, cmap=plt.cm.RdBu,
                  vmax=abs(zGrid).max(), vmin=-abs(zGrid).max())
plt.colorbar()  # draw colorbar

plt.show()

