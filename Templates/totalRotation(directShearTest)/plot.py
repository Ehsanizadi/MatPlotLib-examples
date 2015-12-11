# This code, plots the strain of membrane in 2D extended view (cylindrical membrane conveted to rectangule with width of 2(pi)r and height of Z)
from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np


# Initial settings
fig1 = plt.figure(facecolor='white')

ax1 = plt.subplot2grid((1,1),(0,0))


# Settings for membrane prior to shearing
time, shearingDisp,strain,k25kPa,k50kPa,k100kPa,k150kPa,k200kPa,k300kPa,k500kPa = np.loadtxt('TotalRVERotation.csv', delimiter=',', unpack=True, skiprows=1)


ax1.plot(strain, k25kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k50kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k100kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k150kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k200kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k300kPa, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.plot(strain, k500kPa, label='Shear Stress (kPa)', color='k', linewidth=2)

ax1.set_xlabel('s/d')
ax1.set_ylabel('Total rotation of beads in the proximity of failure plane (deg)')

ax1.spines['left'].set_color('#3a3a3a')
ax1.spines['right'].set_color('#3a3a3a')
ax1.spines['bottom'].set_color('#3a3a3a')
ax1.spines['top'].set_color('#3a3a3a')


ax1.spines['left'].set_linewidth('2.5')
ax1.spines['bottom'].set_linewidth('2.5')
ax1.spines['right'].set_linewidth('2.5')
ax1.spines['top'].set_linewidth('2.5')

ax1.tick_params(axis='x', colors='#3a3a3a')
ax1.tick_params(axis='y', colors='#3a3a3a')

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.15, hspace= 0.2)

ax1.grid(True,color='grey', linestyle=':')
plt.xlim((0,1))
ax1.set_yticks([0,250,500,750,1000,1250,1500])
plt.ylim((0,1500))

plt.show()