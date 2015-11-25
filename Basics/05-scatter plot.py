import matplotlib.pyplot as plt

x=[0,1 ,2 ,3 , 4, 5, 6, 7, 8, 9]
y=[75,74.5,73,67,54,34,12,2,0.5,0]

#  in the scatter function you can set the marker, markers can be '*', 'o', 
#  you can also set the marker size
plt.scatter(x,y,label='my own data', color='black', marker='o', s=30)

plt.xlabel('Deformation (mm)')
plt.ylabel('Shear strength (kPa)')
plt.legend()

plt.show()
