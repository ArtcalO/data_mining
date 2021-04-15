
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
mean_y = mt.art_mean(y)
ecart_type_y = sqrt(var_y)

list_ln_x = mt.ln_list(x)
var_x_prime = mt.variance_list(list_ln_x)
ecart_type_x_prime = sqrt(var_x_prime)
mean_x_prime = mt.art_mean(list_ln_x)

cov_x_prime_y = mt.covariance_list1_list2(list_ln_x,y)

coef_correl_x_prime_y = cov_x_prime_y/(ecart_type_x_prime*ecart_type_y)


print("\nVariance x' = ", var_x_prime)
print("\nVariance y = ", var_y)

print("\nEcart type x' : ", ecart_type_x_prime)
print("\nEcart type y : ", ecart_type_y)

print("\nx' = ", mean_x_prime)
print("\ny = ", mean_y)

print("\n Covariance (x',y) :", cov_x_prime_y)


a = cov_x_prime_y/var_x_prime

b = mean_y-a*mean_x_prime

print("\na = ", a)
print("b = ", b)

print(f"\ny = a*lnx+b")
print(f"\ny = {a}*lnx+{b}")

yr = [1, coef_correl_x_prime_y]
xr = [coef_correl_x_prime_y, 1]

dat_set_r = np.array([yr,xr])

D = mt.determinant_recursive(dat_set_r)

R2 = 1-D

print("R² = ", R2)

