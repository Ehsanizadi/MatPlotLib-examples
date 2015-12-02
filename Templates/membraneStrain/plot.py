# This code, plots the strain of membrane in 2D extended view (cylindrical membrane conveted to rectangule with width of 2(pi)r and height of Z)
from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np


# Initial settings
fig1 = plt.figure(facecolor='white')

# Settings for membrane prior to shearing
x, y, z, deforamtion = np.loadtxt('membraneStrain-final.csv', delimiter=',', unpack=True, skiprows=1)

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
ax1 = plt.contour(xGrid, yGrid, zGrid, 7, linewidths=0.1, colors='grey')
ax1 = plt.contourf(xGrid, yGrid, zGrid, 7, cmap=plt.cm.RdBu,
                  vmax=abs(zGrid).max()/3, vmin=-abs(zGrid).max()/3)
plt.colorbar()  # draw colorbar
plt.title('membrane at the end of shearing')


# for final situation of membrane
fig2 = plt.figure(facecolor='white')
xf, yf, zf, deforamtionf = np.loadtxt('membraneStrain-initial.csv', delimiter=',', unpack=True, skiprows=1)

Zf=zf
Xf=xf
# making X of the plot
for i in range(0,len(xf)): 
	Xf[i] =0 + (i%80) *2.026327262


# Making grid
xGridf = np.linspace(0, 162, 80)
yGridf = np.linspace(-10, 105, 80)
# grid the data.
zGridf = griddata(Xf, zf, deforamtionf, xGridf, yGridf, interp='linear')


# contour the gridded data, plotting dots at the nonuniform data points.
ax1 = plt.contour(xGridf, yGridf, zGridf, 7, linewidths=0.1, colors='grey')
ax1 = plt.contourf(xGridf, yGridf, zGridf, 7, cmap=plt.cm.RdBu,
                  vmax=abs(zGrid).max(), vmin=-abs(zGrid).max())
plt.colorbar()  # draw colorbar
plt.title('membrane prior to shearing')



plt.show()

