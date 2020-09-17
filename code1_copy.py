import numpy as np
import random

random.seed(21)
np.random.seed(21)


ages = [random.randint(10,89) for i in range(10,89)]
#the above code is the short form of the below one
# ages =[]
# for x in range(90):
# 	ages.append( random.randint(10,89) )

net_worths =[ m * 8.78  + abs(np.random.normal(scale = 20.)) for m in ages ]
print(net_worths)
#This is the expansion of the above code
# net_worths =[]
# for m in ages:
# 	net_worths.append(8.78*m + abs(np.random.normal(scale=20.)))

#for the linear regression to work we need to convert the array into 
# rows = total no. of element
# column = 1
#for that we need to use the reshape function in numpy
#but for that we need to change the list into a numpy array 
#np.reshape(numpy_array_name, ( no.of_rows, no.of_columns ) )

ages       = np.reshape( np.array(ages), (len(ages), 2))
net_worths = np.reshape( np.array(net_worths), (len(net_worths), 1))


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

ages_train,ages_test,net_worths_train,net_worths_test = train_test_split(ages,net_worths)

reg = LinearRegression()

reg.fit(ages_train, net_worths_train)

slope = reg.coef_
intercept = reg.intercept_

print("The actuall slope : 8.78")
print("The calculated slope : ", slope)
print("The intercept : ", intercept)

testing_score = round(reg.score(ages_test, net_worths_test),4)
training_score = round(reg.score(ages_train, net_worths_train),4)

print("The scores of the ")
print("Testing data score % :", testing_score*100)
print("Training  data Score % : ", training_score*100)



import matplotlib.pyplot as plt

plt.scatter(ages, net_worths, color='orange',label ='Actuall_data')
plt.plot(ages_test,reg.predict(ages_test),color ='green',label ="Regression_data")
plt.xlabel('Ages')
plt.ylabel('Net Worth')
plt.legend()
plt.show()