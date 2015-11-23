import matplotlib.pyplot as plt

x=[0, 1 ,2 ,3 , 4, 5, 6, 7, 8, 9]
y1=[75 ,74.5,73,67,54  ,34,12,2  ,0.5,0]
y2=[0  ,12  ,24,55,60  ,61,62,62 ,62,62]
y3=[22 ,25  ,27,28,28.1,28,27,24 ,18,16]
y4=[110,100 ,85,30,21.5,30,85,100,110,115]

plt.stackplot(x,y1,y2,y3,y4 , colors=['m','b','r','k'])

plt.xlabel('Deformation (mm)')
plt.ylabel('Shear strength (kPa)')
plt.legend()

plt.show()