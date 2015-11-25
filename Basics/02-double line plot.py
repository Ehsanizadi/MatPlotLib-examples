import matplotlib.pyplot as plt

# data series #1
x1 = [0,1,2,3,4,5]
y1 = [0.14,0.25,0.35,0.3,0.32,0.47]

# data series #2
x2 = x1
y2 = [0.24,0.30,0.35,0.26,0.21,0.13]

# for legends, the data series in 'plot' command, have to be labeled within the 3rd parameter.
plt.plot (x1,y1, label='1st soil sample')
plt.plot (x2,y2, label='2nd soil sample')

# Here is the are for setting axes labels and legend and other plot information data.
# Note that after the command 'plt.show()' the whole package of the plot will be constructed,
# and thats why we should do the manipulating stuff after that command.

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample\nfor new line! (probably I will not need it!)')

plt.legend()
plt.show()