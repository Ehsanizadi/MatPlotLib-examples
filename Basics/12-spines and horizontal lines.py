#  Spines and horizontal lines
import matplotlib.pyplot as plt
import numpy as np

time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('../Text files (data)/data.txt', delimiter=' ', unpack=True, skiprows=1)

fig = plt.figure()

ax1 = plt.subplot2grid((1,1),(0,0))

plt.plot(shearingDisp, shearStress, label='Shear stress (kPa)', color='k', linewidth=2, marker='x', markersize=8, markeredgewidth= 1, markeredgecolor='k', markerfacecolor='b')

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
# plt.title('The stress-strain behaviour of soil sample]')
plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)

ax1.grid(True,color='grey', linestyle=':')

ax1.legend()
plt.show()