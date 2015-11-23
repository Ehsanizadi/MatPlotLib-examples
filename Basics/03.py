import matplotlib.pyplot as plt
# data series #1

x = [2,4,6,8,10]
y = [7,4,10,3,7]

x2 = [1,3,5,7,9]
y2 = [9,3,5,7,2]

# For bar charts, we use 'bar' command instead of 'plot' function
# Another point is that we can change the color of the data series by passing another parameter named color
plt.bar(x,y, label='casual data', color='cyan')
plt.bar(x2,y2, label='anothe casual data', color='grey')

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample\nfor new line! (probably I will not need it!)')

plt.legend()
plt.show()