import matplotlib.pyplot as plt


slices 	= [7,15,32,5,12,22]
mylabels= ['CPT','SPT','Direct shear test','Triaxial test','Vane test','in-situ testing']
mycolors= ['m','r','b','c','g','y']

#  All is self explanatory, one point about explode, it pulls out the element you set non-zero. Just a way to draw the attention
#  of you audience to the "Vane tests". 
#  The parameter 'autopct' adds percentage on the slices.
plt.pie(slices,
		labels=mylabels, 
		colors=mycolors, 
		startangle=30, 
		shadow= True, 
		explode=(0,0,0,0,0.2,0),
		autopct='%1.1f%%')

plt.title('Variety of geotechnical tests in wherever!!')

plt.show()