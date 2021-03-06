#  Basic costimizations

import matplotlib.pyplot as plt
import numpy as np

time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('data.txt', delimiter=' ', unpack=True, skiprows=1)

#  We have to define the plot into a variable to make referencing lot easier!
fig = plt.figure()
# In order to have more than one plots in a figure, the following command is used. (1,1) indicates that the whole figure domain will be divided into 1x1 space (which is one plot! for now!) and it starts from (0,0) which means from the left corner at the bottom.
ax1 = plt.subplot2grid((1,1),(0,0))

plt.plot(shearingDisp, shearStress, label='Shear stress (kPa)', linewidth=2, marker='o', markersize=10, markeredgewidth= 2, markeredgecolor='k', markerfacecolor='y')


plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample]')
#  to set the marginal distances (wspace and hspace are for multiple plots)
plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)
#  in order to have grids
ax1.grid(True,color='r', linestyle='-', linewidth=5)

plt.legend()
plt.show()