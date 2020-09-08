import matplotlib.pyplot as plt
import numpy as np

#linspace returns a list of evenly spaced n number of data | linspace(start_from , end_here, N )
x =np.linspace(0,2,100)


#plt is matplotlib.pyplot as mentioned in the import statement ,
#plt.plot(X_axis,Y_axis,label) is used to plot the values of an array , or arraylike


plt.plot(x,x, label = 'Linear')
plt.plot(x,x**2, label = 'Quadratic')
plt.plot(x,x**3,label='Cubical')

plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Simple')
plt.legend() #used to give the scale 
plt.show()
