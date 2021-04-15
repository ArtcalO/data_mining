# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import pandas as pd
from scipy.stats import linregress
import scipy.stats

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

##############################################################################
##############################################################################

print("\n Les Coefficient de corelations")
print("----------------------------------")

print("Coefficient de corelation simple demandée")
print("-----------------------------------------\n")
print("r = %s" % np.corrcoef(x,y)[0,1])

print("\ncoefficient de corelation de pearson")
print("-----------------------------------------")
print(f"r = {scipy.stats.pearsonr(x, y)[0]}")
print("\ncoefficient de corelation de spearmanr")
print("-----------------------------------------")
print(f"r= {scipy.stats.spearmanr(x, y)[0]}")
print("\ncoefficient de corelation de pearson")
print("-----------------------------------------")
print(f"r = {scipy.stats.kendalltau(x, y)[0]}")

print("\n")



##############################################################################
##############################################################################

"""
create a function to fit with your data. a, b, c and d are the \ncoefficients
that curve_fit will calculate for you. 
In this part you need to guess and/or use mathematical knowledge to find
a function that resembles your data
"""
def func(x, a, b, c, d, e, f, g, h, i):
	return a*x**8+b*x**7+c*x**6+d*x**5+e*x**4+f*x**3+g*x**2+h*x+i


"""
make the curve_fit
"""
popt, pcov = curve_fit(func, x, y)

"""
The result is:
popt[0] = a , popt[1] = b, popt[2] = c and popt[3] = d of the function,
so f(x) = popt[0]*x**3 + popt[1]*x**2 + popt[2]*x + popt[3].
"""
print("a = %s , b = %s, c = %s, d = %s, e = %s, f = %s, g = %s, h = %s, i = %s" % (popt[0], popt[1], popt[2], popt[3],popt[4],popt[5],popt[6],popt[7],popt[8]))

"""
Use sympy to generate the latex sintax of the function
"""
# xs = sym.Symbol('\nlambda')    
# tex = sym.latex(func(xs,*popt)).replace('$', '')
# plt.title(r'$f(\nlambda)= %s$' %(tex),fontsize=16)

"""
Print the coefficients and plot the funcion.
"""

# plt.plot(x, func(x, *popt), label="Fitted Curve") #same as line above \/
# #plt.plot(x, popt[0]*x**3 + popt[1]*x**2 + popt[2]*x + popt[3], label="Fitted Curve") 

# plt.legend(loc='upper left')
# plt.show()
