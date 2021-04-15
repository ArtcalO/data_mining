from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

#----------------------------------------------------------------------------------------#
# Step 1: training data

data_set = pd.read_excel("Données.xls")
data_set = np.array(data_set)
X=data_set[:,0]
Y=data_set[:,1]

X = np.asarray(X)
Y = np.asarray(Y)

X = X[:,np.newaxis]
Y = Y[:,np.newaxis]

print(X)
print(Y)

plt.scatter(X,Y)

#----------------------------------------------------------------------------------------#
# Step 2: data preparation

nb_degree = int(input("Entrer le degre : "))

polynomial_features = PolynomialFeatures(degree = nb_degree)

X_TRANSF = polynomial_features.fit_transform(X)

#----------------------------------------------------------------------------------------#
# Step 3: define and train a model

model = LinearRegression()

model.fit(X_TRANSF, Y)

#----------------------------------------------------------------------------------------#
# Step 4: calculate bias and variance

Y_NEW = model.predict(X_TRANSF)

rmse = np.sqrt(mean_squared_error(Y,Y_NEW))
r2 = r2_score(Y,Y_NEW)

print('RMSE: ', rmse)
print('R2: ', r2)

#----------------------------------------------------------------------------------------#
# Step 5: prediction

x_new_min = 0.0
x_new_max = 10.0

X_NEW = np.linspace(x_new_min, x_new_max, 100)
X_NEW = X_NEW[:,np.newaxis]

X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)

Y_NEW = model.predict(X_NEW_TRANSF)

plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)

plt.grid()
plt.xlim(x_new_min,x_new_max)
plt.ylim(0,10)

title = 'Degree = {}; RMSE = {}; R2 = {}'.format(nb_degree, round(rmse,2), round(r2,2))

plt.title("Polynomial Linear Regression using scikit-learn and python 3 \n " + title,
          fontsize=10)
plt.xlabel('x')
plt.ylabel('y')

plt.savefig("polynomial_linear_regression.png", bbox_inches='tight')
plt.show()