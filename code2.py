import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0,10.0)

#Reading data

data = pd.read_csv('data.csv')
print(data.shape)

print(data.head())

#collecting the x and y values
X = data['experience'].values
Y = data['salary'].values

#to get the equation of the regression line y = mx + c ,
#we need to find the value of slope first
# m = Sum{ ([X-mean_x] * [Y - mean_y]) } / Sum { [X - mean_x]**2 }

#calculating the mean

mean_x =np.mean(X)
mean_y =np.mean(Y)

#collecting the total number of values so that we can minus the mean from everything

n = len(X)

# Lets consider m = numerator / denominator , we they each take the respective
#positions as mentioned in l20 equation

numerator, denominator = 0 , 0

for i in range(n):
	numerator += (X[i] - mean_x)*(Y[i] - mean_y)
	denominator += (X[i]-mean_x)**2



# lets get the value of m and c || y = mx + c
m = numerator/denominator
# from y = mx + c || c = y - mx
c = mean_y - (m*mean_x)


print(" m = {} and c = {} ".format(m,c))

#plotting Values and regression line

max_x = np.max(X) + 10
min_x = np.min(X) - 10

#calculating line values x and y

x = np.linspace(min_x, max_x,100)
y = m*x + c

#Rsquared method , did'nt understand this part

ss_t , ss_r= 0,0

for i in range(n):
	y_pred = m + X[i]*c
	ss_t += (Y[i] - mean_y)**2
	ss_r += (Y[i]- y_pred)**2

r2 = 1 -(ss_r/ss_t)
print("R2 = ",r2)

#plotting line

plt.plot(x,y, color ="#58b970", label= "Regression Line")

#plotting scatter points
plt.scatter(X, Y, c="#ef5423", label="Scatter Plots")

plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()












