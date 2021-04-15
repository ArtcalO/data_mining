import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

data_set = pd.read_excel("Données.xls")
data_set = np.array(data_set)


# Fit the function y = A * exp(B * x) to the data
# returns (A, B)
# From: https://mathworld.wolfram.com/LeastSquaresFittingExponential.html
def fit_exp(xs, ys):
    S_x2_y = 0.0
    S_y_lny = 0.0
    S_x_y = 0.0
    S_x_y_lny = 0.0
    S_y = 0.0
    for (x,y) in zip(xs, ys):
        S_x2_y += x * x * y
        S_y_lny += y * np.log(y)
        S_x_y += x * y
        S_x_y_lny += x * y * np.log(y)
        S_y += y
    #end
    a = (S_x2_y * S_y_lny - S_x_y * S_x_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
    b = (S_y * S_x_y_lny - S_x_y * S_y_lny) / (S_y * S_x2_y - S_x_y * S_x_y)
    print(a)
    print(b)
    print((np.exp(a), b))
    return (np.exp(a), b)


xs=data_set[:,0]
ys=data_set[:,1]

(A, B) = fit_exp(xs, ys)

plt.figure()
plt.plot(xs, ys, 'o-', label='Raw Data')
plt.plot(xs, [A * np.exp(B *x) for x in xs], 'o-', label='Fit')

plt.title('Exponential Fit Test')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best')
plt.tight_layout()
plt.show()