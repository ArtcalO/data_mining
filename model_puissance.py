
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


list_ln_y = mt.ln_list(y)
list_ln_x = mt.ln_list(x)

var_y_prime = mt.variance_list(list_ln_y)
var_x_prime = mt.variance_list(list_ln_x)

ecart_type_y_prime = sqrt(var_y_prime)
ecart_type_x_prime = sqrt(var_x_prime)


mean_y_prime = mt.art_mean(list_ln_y)
mean_x_prime = mt.art_mean(list_ln_x)

cov_x_prime_y_prime = mt.covariance_list1_list2(list_ln_x,list_ln_y)

coef_correl_x_prime_y_prime = cov_x_prime_y_prime/(ecart_type_x_prime*ecart_type_y_prime)


print("\nVariance x' = ", var_x_prime)
print("\nVariance y' = ", var_y_prime)

print("\nEcart type x' : ", ecart_type_x_prime)
print("\nEcart type y' : ", ecart_type_y_prime)

print("\nx' = ", mean_x_prime)
print("\ny' = ", mean_y_prime)

print("\n Covariance (x',y') :", cov_x_prime_y_prime)


a = cov_x_prime_y_prime/var_x_prime

b_prime = mean_y_prime-a*mean_x_prime

print("b' = ", b_prime)

b = np.exp(b_prime)

print("\na = ", a)
print("b = ", b)

print(f"\ny = b*x**a")
print(f"\ny = {b}*x**{a}")

yr = [1, coef_correl_x_prime_y_prime]
xr = [coef_correl_x_prime_y_prime, 1]

dat_set_r = np.array([yr,xr])

D = mt.determinant_recursive(dat_set_r)

R2 = 1-D

print("R² = ", R2)

