
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from scipy.stats import linregress
import meantools as mt
from math import sqrt

data_set = pd.read_excel("Données.xls")
data_set = np.array(data_set)
# import sympy as sym

"""
Generate some data, let's imagine that you already have this. 
"""
x=data_set[:,0]
y =data_set[:,1]



"""
Plot your data
"""
plt.plot(x, y, 'ro',label="Original Data")

"""
brutal force to avoid errors
"""    
x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
y = np.array(y, dtype=float) #so the curve_fit can work



var_y = mt.variance_list(y)
var_x = mt.variance_list(x)

print("\nVariance x : ", var_x)
print("\nVariance y : ", var_y)

mean_y = mt.art_mean(y)
mean_x = mt.art_mean(x)

print("\nMoyenne x : ", mean_x)
print("\nMoyenne y : ", mean_y)

cov_x_y = mt.covariance_list1_list2(x,y)
print("\n Covariance (x,y) :", cov_x_y)


a = (var_y-var_x+sqrt(((var_y-var_x)**2)+(4*(cov_x_y**2))))/(2*cov_x_y)
print("\n Les coefficients de la droite de regression orthogonale sont :")
print("a = ", a)

b = mean_y-a*mean_x

print("b = ", b)
print(f"\n y = {a}x{b}")

