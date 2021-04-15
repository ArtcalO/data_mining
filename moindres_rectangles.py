# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from scipy.stats import linregress
import math
import meantools as mt

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
data_set_x1 = np.array(x, dtype=float) #transform your data in a numpy array of floats 
data_set_y = np.array(y, dtype=float) #so the curve_fit can work



arth_mean_x1 = mt.art_mean(data_set_x1)

arth_mean_y = mt.art_mean(data_set_y)

# geo_mean_x = mt.geo_mean(data_set_x)
# geo_mean_y = mt.geo_mean(data_set_y)

sum_x1_pow_2 = mt.sum_list_square(data_set_x1)

sum_y_pow_2 = mt.sum_list_square(data_set_y)

sum_x1 = mt.sum_list(data_set_x1)

sum_y = mt.sum_list(data_set_y)

sum_x1_y = mt.sum_list1_dot_list2(data_set_x1,data_set_y)


var_x1 = mt.variance_list(data_set_x1)

var_y = mt.variance_list(data_set_y)

cov_x1_y = mt.covariance_list1_list2(data_set_x1,data_set_y)


# a= cov_x_y/var_x
# b = arth_mean_y-a*arth_mean_x

# e = mt.get_e(data_set_x,data_set_y,a,b)

#recherche des ecart types 
ecart_x1 = math.sqrt(var_x1)

ecart_y= math.sqrt(var_y)



# rd = pow(r,2)
# ve = mt.var_expliquee(ecart_y, r)
# vre = mt.var_residuelle(ecart_y, r)

# variance_x = []
# sigma_x = []
# z_i = []

print("Pour x1 la moyenne arithmetiques est : ", arth_mean_x1)

print("Pour y la moyenne arithmetiques est : ", arth_mean_y)

# print("Pour x la moyenne arithmetiques est : ", geo_mean_x)
# print("Pour y la moyenne arithmetiques est : ", geo_mean_y)



print("\nVariance x1 : ", var_x1)

print("\nVariance y : ", var_y)

print("\nCovariance x1 et y : ", cov_x1_y)


print("\nEcart type  x1 : ", ecart_x1)

print("\nEcart type  y : ", ecart_y)

a = ecart_y/ecart_x1

b = arth_mean_y-(a*arth_mean_x1)

print("a = {0:.13f}".format(a))
print("a = {0:.13f}".format(b))

