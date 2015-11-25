#  load data from file: The CSV approach

import matplotlib.pyplot as plt
import csv

x = [] # shearing displacement
y = [] # shear strength
z = [] # topPlate vertical displacement

with open('../Text files (data)/data.txt', 'r') as csvfile:
	# to ignore the first line! (the first line contains headers which are the titles of each column)
	next(csvfile, None)
	source = csv.reader(csvfile, delimiter = ' ')
	for row in source:
		if row > 1:
			x.append(float(row[1]))
			y.append(float(row[6]))
			z.append(float(row[2]))

plt.plot(x,y, label='Shear stress (kPa)')
plt.plot(x,z, label='dilation(mm)')

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample]')

plt.legend()
plt.show()