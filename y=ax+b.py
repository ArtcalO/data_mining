import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

data_set = pd.read_excel("Données.xls")
data_set = np.array(data_set)
x=data_set[:,0]
y=data_set[:,1]

print(x)
print(y)

parametres = np.polyfit(x, y, 1)
print(parametres)

a, b, r, p_vall, std_err = linregress(x, y)
print("a = ", a, " b = ", b, " r^2 = ", r**2)