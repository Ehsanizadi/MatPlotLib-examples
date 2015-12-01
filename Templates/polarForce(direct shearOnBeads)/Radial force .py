#  Subplots (important)
import matplotlib.pyplot as plt
import numpy as np
# To add polar chart settings (which is not available by matplotlib now!)
from polarSettings import fractional_polar_axes

fig = plt.figure(facecolor='white')

# All settings for AX1
shearDisp, angle, contactForce = np.loadtxt('polarForceData.0.csv', delimiter=' ', unpack=True, skiprows=1)

ax1 = fractional_polar_axes(fig, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax1.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.fill_between(angle, contactForce, color = 'grey' , alpha=1)

# plt.subplots_adjust(left=0.1, bottom= 0.12, right= 0.9, top=0.91, wspace=0.15, hspace= 0.2)

plt.show()


# All settings for AX2
shearDisp, angle, contactForce = np.loadtxt('polarForceData.1.csv', delimiter=' ', unpack=True, skiprows=1)

ax1 = fractional_polar_axes(fig, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax1.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.fill_between(angle, contactForce, color = 'grey' , alpha=1)

# plt.subplots_adjust(left=0.1, bottom= 0.12, right= 0.9, top=0.91, wspace=0.15, hspace= 0.2)

plt.show()
