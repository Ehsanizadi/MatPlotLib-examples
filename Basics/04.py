import matplotlib.pyplot as plt
# data series #1

population_ages = [74,56,42,42,95,111,112,132,99,75,65,63,12,4,64,54,32,25,22,39,37,47,65,12,55,72,57,73,49,51,65,56,55,66]

# ids = [x for x in range(len(population_ages))]

# In bins the all data from 0 to 9 will be put in "0" and all data from 10 - 19 will be put in "10" , and etc.
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

# plt.bar(ids, population_ages, label='people ages histogram', color = 'black')

plt.hist(population_ages, bins, histtype='bar', rwidth=0.9)

plt.xlabel('Shear deformation (mm)')
plt.ylabel('Shear stress (GPa)')
plt.title('The stress-strain behaviour of soil sample\nfor new line! (probably I will not need it!)')

plt.legend()
plt.show()