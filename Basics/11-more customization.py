#  More customization of colors and fills 
import matplotlib.pyplot as plt
import numpy as np

time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('../Text files (data)/data.txt', delimiter=' ', unpack=True, skiprows=1)

fig = plt.figure()

ax1 = plt.subplot2grid((1,1),(0,0))

plt.plot(shearingDisp, shearStress, label='Shear stress (kPa)', color='k', linewidth=2, marker='x', markersize=8, markeredgewidth= 1, markeredgecolor='k', markerfacecolor='b')
#  To fill the subsurface of the plot (the 3rd parameter indicates the base line for filling) (Alpha indicates the degree of the opaqueness)
ax1.fill_between(shearingDisp, shearStress, 70 , alpha=0.3)


plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
# plt.title('The stress-strain behaviour of soil sample]')
plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)

ax1.grid(True,color='grey', linestyle=':')

# To change the color of the axes labels
ax1.xaxis.label.set_color('r')
ax1.yaxis.label.set_color('c')

# To set the tick marks as specific as you want:
ax1.set_yticks([0,50,100,150,200])

ax1.legend()
plt.show()