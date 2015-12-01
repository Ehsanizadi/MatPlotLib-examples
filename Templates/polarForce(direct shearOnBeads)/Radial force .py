#  Subplots (important)
import matplotlib.pyplot as plt
import numpy as np
# To add polar chart settings (which is not available by matplotlib now!)
from polarSettings import fractional_polar_axes


# All settings for AX1
fig1 = plt.figure(facecolor='white')

shearDisp, angle, contactForce = np.loadtxt('polarForceData.0.csv', delimiter=' ', unpack=True, skiprows=1)

ax1 = fractional_polar_axes(fig1, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax1.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax1.fill_between(angle, contactForce, color = 'grey' , alpha=1)
plt.title('s/d = 0', y=1.08)

# All settings for AX2
fig2 = plt.figure(facecolor='white')

shearDisp, angle, contactForce = np.loadtxt('polarForceData.1.csv', delimiter=' ', unpack=True, skiprows=1)

ax2 = fractional_polar_axes(fig2, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax2.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax2.fill_between(angle, contactForce, color = 'grey' , alpha=1)
plt.title('s/d = 0.025', y=1.08)

# All settings for AX3
fig3 = plt.figure(facecolor='white')

shearDisp, angle, contactForce = np.loadtxt('polarForceData.10.csv', delimiter=' ', unpack=True, skiprows=1)

ax3 = fractional_polar_axes(fig3, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax3.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax3.fill_between(angle, contactForce, color = 'grey' , alpha=1)
plt.title('s/d = 0.25', y=1.08)


# All settings for AX4
fig4 = plt.figure(facecolor='white')

shearDisp, angle, contactForce = np.loadtxt('polarForceData.20.csv', delimiter=' ', unpack=True, skiprows=1)

ax4 = fractional_polar_axes(fig4, thlim=(0, 180), rlim=(0, 4000), rlabel='Normal force (N)', thlabel='', ticklabels=True, step=(30, 1000))
ax4.plot(angle, contactForce, label='Shear Stress (kPa)', color='k', linewidth=2)
ax4.fill_between(angle, contactForce, color = 'grey' , alpha=1)
plt.title('s/d = 0.5', y=1.08)


plt.show()

