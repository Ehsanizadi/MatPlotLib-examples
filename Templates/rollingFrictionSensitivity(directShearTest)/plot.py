import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(facecolor='white')

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

strain,stress0,dilation0,rotation0,stress0025,dilation0025,rotation0025,stress1,dilation1,rotation1 = np.loadtxt('rollingFrictionSensitivity.csv', delimiter=',', unpack=True, skiprows=1)

# All settings for AX1
ax1.plot(strain, stress0, label='Cr = 0.0', color='grey', linewidth=3)
ax1.plot(strain, stress0025, label='Cr = 0.0025', color='red', linewidth=1)
ax1.plot(strain, stress1, label='Cr = 0.1', color='blue', linewidth=2, linestyle='--')

ax1.set_xlabel('s/d')
ax1.set_ylabel('Shear stress (kPa)')

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

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.2, hspace= 0.2)

ax1.grid(True,color='grey', linestyle=':')
ax1.set_xlim([0,1])

ax1.legend(loc = 'best')

# All settings for AX2
ax2.plot(strain, dilation0, label='Cr = 0.0', color='grey', linewidth=3)
ax2.plot(strain, dilation0025, label='Cr = 0.0025', color='red', linewidth=1)
ax2.plot(strain, dilation1, label='Cr = 0.1', color='blue', linewidth=2, linestyle='--')
ax2.set_xlabel('s/d')
ax2.set_ylabel('Top plate upward \ndisplacement (mm)')

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

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.2, hspace= 0.2)

ax2.grid(True,color='grey', linestyle=':')
ax2.set_xlim([0,1])
ax2.set_ylim([0,0.2])


# All settings for AX3
ax3.plot(strain, rotation0, label='Cr = 0.0', color='grey', linewidth=3)
ax3.plot(strain, rotation0025, label='Cr = 0.0025', color='red', linewidth=1)
ax3.plot(strain, rotation1, label='Cr = 0.1', color='blue', linewidth=2, linestyle='--')
ax3.set_xlabel('s/d')
ax3.set_ylabel('Total rotation of beads in the \n proximity of failure plane (deg)')

ax3.spines['left'].set_color('#3a3a3a')
ax3.spines['right'].set_color('#3a3a3a')
ax3.spines['bottom'].set_color('#3a3a3a')
ax3.spines['top'].set_color('#3a3a3a')


ax3.spines['left'].set_linewidth('2.5')
ax3.spines['bottom'].set_linewidth('2.5')
ax3.spines['right'].set_linewidth('2.5')
ax3.spines['top'].set_linewidth('2.5')

ax3.tick_params(axis='x', colors='#3a3a3a')
ax3.tick_params(axis='y', colors='#3a3a3a')

plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.2, hspace= 0.2)

ax3.grid(True,color='grey', linestyle=':')

ax3.set_xlim([0,1])
ax3.set_ylim([0,2000])


plt.show()