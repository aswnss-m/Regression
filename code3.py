from sklearn.neighbors import KNeighborsClassifier
import random
import matplotlib.pyplot as plt
random.seed(40)

X,Y = [],[]

for i in range(5):
	X.append([random.randint(2,20)])

for i in range(5):
	Y.append(random.randint(0,1))


neigh =KNeighborsClassifier(n_neighbors=2)
neigh.fit(X, Y)
print(neigh.predict([[30.1],[2.3],[15.3],[7.9]]))