import math
import numpy as np
import pandas as pd

def art_mean(dt):
	s=0
	for x in dt:
		s=s+x

	mean = s/len(dt)

	return mean

def geo_mean(dt):
	p = 1
	for x in dt:
		p=p*x
	mean = pow(p, 1/len(dt))
	return mean

def har_mean(dt):
	pass

def quad_mean(dt):
	pass

def mediane():
	pass
def mode():
	pass

def sum_list(x):
	s=0
	for i in x:
		s=s+i
	return s

def sum_list_to_expo(x, exp):
	s=0
	for i in x:
		s=s+(i**exp)
	return s

def sum_list_square(x):
	s=0
	for i in x:
		s=s+(i**2)
	return s

def sum_list1_dot_list2(x,y):
	ss=[]
	for i in range(len(x)):
		for j in range(len(y)):
			if(i==j):
				ss.append(x[i]*y[j])

	s=sum_list(ss)
	return s

def sum_list1_pow_dot_list2(x,y, exp):
	ss=[]
	for i in range(len(x)):
		for j in range(len(y)):
			if(i==j):
				ss.append((x[i]**exp)*y[j])

	s=sum_list(ss)
	return s

# for x in data_set_x:
# 	variance_x.append((1/len(data_set_x)*pow((x-arth_mean_x),2)))

def variance_list(x):
	variance_x=[]
	for i in x:
		variance_x.append((1/len(x)*pow((i-art_mean(x)),2)))
	var_x = sum_list(variance_x)
	return var_x

def covariance_list1_list2(x, y):
	cov_list = []
	for i in range(len(x)):
		for j in range(len(y)):
			if i==j :
				cov_list.append((1/len(x)*((x[i]-art_mean(x))*(y[j]-art_mean(y)))))
	cov_x_y = sum_list(cov_list)

	return cov_x_y

def y_hat(a,x,b):
		return a*x+b

def get_e(x,y, a,b):
	e_list=[]
	for j in range(len(y)):
		for i in range(len(x)):
			e_list.append((1/len(y))*((y[j]-y_hat(a,x[i],b))**2))
	e= math.sqrt(sum_list(e_list))
	return e

def corr_coeffiscient(cov, ecart_x, ecart_y):
	return cov/(ecart_x*ecart_y)

def var_expliquee(ecart_y, r):
	return pow(ecart_y,2)*pow(r,2)

def var_residuelle(ecart_y, r):
	return pow(ecart_y,2)*(1-pow(r,2))


def ln_list(x):
	ln_liste=[]
	for i in x:
		ln_liste.append(np.log(i))
	return ln_liste

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: A copy of the given matrix
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)

    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

def determinant_recursive(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
     
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    # Section 3: define submatrix for focus column and 
    #      call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = copy_matrix(A) # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D) 
 
        for i in range(height): 
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) # F) 
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det 
 
    return total




