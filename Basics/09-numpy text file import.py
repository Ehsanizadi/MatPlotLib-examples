#  load data from file: The numpy approach (BETTER APPROACH! TRUST ME! ;-) )

import matplotlib.pyplot as plt
import numpy as np

# You have to declare the same number f variables as you have in the text file
# 'skiprows' ignores the header (the first line)
time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('data.txt', delimiter=' ', unpack=True, skiprows=1)

plt.plot(shearingDisp, shearStress, label='Shear stress (kPa)', linewidth=2, marker='o', markersize=10, markeredgewidth= 2, markeredgecolor='k', markerfacecolor='y')


plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample]')

plt.legend()
plt.show()