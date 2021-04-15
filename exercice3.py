
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




var_x = mt.variance_list(x)

mean_x = mt.art_mean(x)

list_ln_y = mt.ln_list(y)

var_y_prime = mt.variance_list(list_ln_y)

ecart_type_y_prime = sqrt(var_y_prime)
ecart_type_x = sqrt(var_x)

mean_y_prime = mt.art_mean(list_ln_y)

cov_x_y_prime = mt.covariance_list1_list2(x,list_ln_y)

coef_correl_x_y_prime = cov_x_y_prime/(ecart_type_x*ecart_type_y_prime)

print("\nMoyenne x : ", mean_x)
print("\nVariance x : ", var_x)
print("\nVariance y' = ", var_y_prime)
print("\ny' = ", mean_y_prime)
print("\n Covariance (x,y') :", cov_x_y_prime)
print("\nEcart type x : ", ecart_type_x)
print("\nEcart type y' : ", ecart_type_y_prime)

a_prime = cov_x_y_prime/var_x
a = np.exp(a_prime)

b_prime = mean_y_prime-a*mean_x

print("b' = ", b_prime)

b = np.exp(b_prime)

print("\na = ", a)
print("b = ", b)

print(f"\ny= b*e**a*x")
print(f"\ny = {b}e**{a}*x")

R = cov_x_y_prime/(ecart_type_y_prime*ecart_type_x)

print("R = ", R)





