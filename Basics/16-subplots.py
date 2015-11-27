#  Subplots (important)
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(facecolor='white')

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('../Text files (data)/data.txt', delimiter=' ', unpack=True, skiprows=1)

# All settings for AX1
ax1.plot(shearingDisp, shearStress, label='Shear Stress (kPa)', color='k', linewidth=2, marker='x', markersize=8, markeredgewidth= 1, markeredgecolor='k',markerfacecolor='b')

ax1.set_xlabel('Shear deformation (mm)')
ax1.set_ylabel('Shear stress (GPa)')

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

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)

ax1.grid(True,color='grey', linestyle=':')

ax1.legend(loc = 'best')

# All settings for AX2
ax2.plot(shearingDisp, verticalDisp, label='Dilation (mm)', color='k', linewidth=2)

ax2.set_xlabel('Shear deformation (mm)')
ax2.set_ylabel('Top plate upward displacement (mm)')

ax2.spines['left'].set_color('#3a3a3a')
ax2.spines['right'].set_color('#3a3a3a')
ax2.spines['bottom'].set_color('#3a3a3a')
ax2.spines['top'].set_color('#3a3a3a')


ax2.spines['left'].set_linewidth('2.5')
ax2.spines['bottom'].set_linewidth('2.5')
ax2.spines['right'].set_linewidth('2.5')
ax2.spines['top'].set_linewidth('2.5')

ax2.tick_params(axis='x', colors='#3a3a3a')
ax2.tick_params(axis='y', colors='#3a3a3a')

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)

ax2.grid(True,color='grey', linestyle=':')

ax2.legend(loc = 'best')



plt.show()