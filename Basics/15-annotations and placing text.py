#  Annotations and placing text on graph
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')


time, shearingDisp, verticalDisp, fsf, rsf, totalForce, shearStress, manifold, contact, CN = np.loadtxt('../Text files (data)/data.txt', delimiter=' ', unpack=True, skiprows=1)

fig = plt.figure()

ax1 = plt.subplot2grid((1,1),(0,0))

plt.plot(shearingDisp, shearStress, label='Shear stress (kPa)', color='k', linewidth=2, marker='x', markersize=8, markeredgewidth= 1, markeredgecolor='k', markerfacecolor='b')

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')

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




# In order to change font and textual customizations you can define fontDicts and use them.
# Available font families: 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'
myOwnFontDict= {'family':'sans-serif', 'color':'green', 'size':20}
myOwnFontDict2= {'family':'cursive', 'color':'black', 'size':20}

# Here you can add texts to your plots based on the coordinates you used for data plottting
ax1.text(shearingDisp[10], shearStress[3], 'My own text!', fontdict=myOwnFontDict)
ax1.text(shearingDisp[10], shearStress[0], 'My own text!', fontdict=myOwnFontDict2)

# To print data points!, possibly worthless
'''for i in range(len(shearingDisp)):
	ax1.text(shearingDisp[i], shearStress[i], shearStress[i])
'''
plt.subplots_adjust(left=0.1, bottom= 0.1, right= 0.95, top=0.95, wspace=0.1, hspace= 0.1)

ax1.grid(True,color='grey', linestyle=':')

ax1.legend()
plt.show()