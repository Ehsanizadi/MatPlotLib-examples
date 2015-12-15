from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np


# Initial settings
fig1 = plt.figure(facecolor='white')

ax1 = plt.subplot2grid((1,1),(0,0))


# Settings for membrane prior to shearing
Time,Extension,ThinMembraneLoad,ThickMembraneLoad = np.loadtxt('membraneTensionTest.csv', delimiter=',', unpack=True, skiprows=1)

initialLength = 100 # in mmm
strain = Extension / 100

ax1.plot(strain, ThinMembraneLoad, label='Thin membrane', color='blue', linewidth=2)
ax1.plot(strain, ThickMembraneLoad, label='Thick membrane', color='red', linewidth=2)


ax1.set_xlabel('Strain (not in precent)')
ax1.set_ylabel('Load (N)')

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
plt.xlim((0,0.6))
# ax1.set_yticks([0,250,500,750,1000,1250,1500])
# plt.ylim((0,1500))
ax1.legend(loc = 'best')

plt.show()