import meantools as mt
import math
import numpy as np

data_set_x1 = [2310,2333,2356,2379,2402,2425,2448,2471,2494,2517,2540]
data_set_x2 = [2,2,3,3,2,4,2,2,3,4,2]
data_set_x3 = [2,2,1,2,3,2,1,2,3,4,3]
data_set_x4 = [20,12,33,43,53,23,99,34,23,55,22]




# data_set_x = [138.08,100.37, 37.52, 34.9, 204.4, 95, 38]

data_set_y = [142000,144000,151000,150000,139000,169000,126000,142900,163000,169000,149000]
# data_set_y = [73.13,56.56, 21.48,16.81,115.56,53.7,20.15]

arth_mean_x1 = mt.art_mean(data_set_x1)
arth_mean_x2 = mt.art_mean(data_set_x2)
arth_mean_x3 = mt.art_mean(data_set_x3)
arth_mean_x4 = mt.art_mean(data_set_x4)
arth_mean_y = mt.art_mean(data_set_y)

# geo_mean_x = mt.geo_mean(data_set_x)
# geo_mean_y = mt.geo_mean(data_set_y)

sum_x1_pow_2 = mt.sum_list_square(data_set_x1)
sum_x2_pow_2 = mt.sum_list_square(data_set_x2)
sum_x3_pow_2 = mt.sum_list_square(data_set_x3)
sum_x3_pow_4 = mt.sum_list_square(data_set_x4)
sum_y_pow_2 = mt.sum_list_square(data_set_y)

sum_x1 = mt.sum_list(data_set_x1)
sum_x2 = mt.sum_list(data_set_x2)
sum_x3 = mt.sum_list(data_set_x3)
sum_x4 = mt.sum_list(data_set_x4)
sum_y = mt.sum_list(data_set_y)

sum_x1_y = mt.sum_list1_dot_list2(data_set_x1,data_set_y)
sum_x2_y = mt.sum_list1_dot_list2(data_set_x2,data_set_y)
sum_x3_y = mt.sum_list1_dot_list2(data_set_x3,data_set_y)
sum_x4_y = mt.sum_list1_dot_list2(data_set_x4,data_set_y)
sum_x1_x2 = mt.sum_list1_dot_list2(data_set_x1,data_set_x2)
sum_x1_x3 = mt.sum_list1_dot_list2(data_set_x1,data_set_x3)
sum_x1_x4 = mt.sum_list1_dot_list2(data_set_x1,data_set_x3)
sum_x2_x3 = mt.sum_list1_dot_list2(data_set_x2,data_set_x3)
sum_x2_x4 = mt.sum_list1_dot_list2(data_set_x2,data_set_x3)
sum_x3_x4 = mt.sum_list1_dot_list2(data_set_x2,data_set_x3)

var_x1 = mt.variance_list(data_set_x1)
var_x2 = mt.variance_list(data_set_x2)
var_x3 = mt.variance_list(data_set_x3)
var_x4 = mt.variance_list(data_set_x4)
var_y = mt.variance_list(data_set_y)

cov_x1_y = mt.covariance_list1_list2(data_set_x1,data_set_y)
cov_x2_y = mt.covariance_list1_list2(data_set_x2,data_set_y)
cov_x3_y = mt.covariance_list1_list2(data_set_x3,data_set_y)
cov_x4_y = mt.covariance_list1_list2(data_set_x4,data_set_y)
cov_x1_x2 = mt.covariance_list1_list2(data_set_x1,data_set_x2)
cov_x1_x3 = mt.covariance_list1_list2(data_set_x1,data_set_x3)
cov_x1_x4 = mt.covariance_list1_list2(data_set_x1,data_set_x4)
cov_x2_x3 = mt.covariance_list1_list2(data_set_x2,data_set_x3)
cov_x2_x4 = mt.covariance_list1_list2(data_set_x2,data_set_x4)
cov_x3_x4 = mt.covariance_list1_list2(data_set_x3,data_set_x4)

# a= cov_x_y/var_x
# b = arth_mean_y-a*arth_mean_x

# e = mt.get_e(data_set_x,data_set_y,a,b)

#recherche des ecart types 
ecart_x1 = math.sqrt(var_x1)
ecart_x2 = math.sqrt(var_x2)
ecart_x3 = math.sqrt(var_x3)
ecart_x4 = math.sqrt(var_x4)
ecart_y= math.sqrt(var_y)

ryx1 = mt.corr_coeffiscient(cov_x1_y, ecart_y, ecart_x1)
ryx2 = mt.corr_coeffiscient(cov_x2_y, ecart_y,ecart_x2)
ryx3 = mt.corr_coeffiscient(cov_x3_y, ecart_y,ecart_x3)
ryx4 = mt.corr_coeffiscient(cov_x4_y, ecart_y,ecart_x4)
rx1x2 = mt.corr_coeffiscient(cov_x1_x2, ecart_x1, ecart_x2)
rx1x3 = mt.corr_coeffiscient(cov_x1_x3, ecart_x1, ecart_x3)
rx1x4 = mt.corr_coeffiscient(cov_x1_x4, ecart_x1, ecart_x4)
rx2x3 = mt.corr_coeffiscient(cov_x2_x3, ecart_x2, ecart_x3)
rx2x4 = mt.corr_coeffiscient(cov_x2_x4, ecart_x2, ecart_x4)
rx3x4 = mt.corr_coeffiscient(cov_x3_x4, ecart_x3, ecart_x4)

# rd = pow(r,2)
# ve = mt.var_expliquee(ecart_y, r)
# vre = mt.var_residuelle(ecart_y, r)

# variance_x = []
# sigma_x = []
# z_i = []

print("Pour x1 la moyenne arithmetiques est : ", arth_mean_x1)
print("Pour x2 la moyenne arithmetiques est : ", arth_mean_x2)
print("Pour x3 la moyenne arithmetiques est : ", arth_mean_x3)
print("Pour x4 la moyenne arithmetiques est : ", arth_mean_x4)
print("Pour y la moyenne arithmetiques est : ", arth_mean_y)

# print("Pour x la moyenne arithmetiques est : ", geo_mean_x)
# print("Pour y la moyenne arithmetiques est : ", geo_mean_y)


print("\nSomme x1² : ", sum_x1_pow_2)
print("\nSomme x2² : ", sum_x2_pow_2)
print("\nSomme x3² : ", sum_x3_pow_2)
print("\nSomme y² : ", sum_y_pow_2)
print("\nSomme x1 : ", sum_x1)
print("\nSomme x2 : ", sum_x2)
print("\nSomme x3 : ", sum_x3)
print("\nSomme y : ", sum_y)
print("\nSomme x1*y : ", sum_x1_y)
print("\nSomme x2*y : ", sum_x2_y)
print("\nSomme x3*y : ", sum_x3_y)
print("\nSomme x1*x2 : ", sum_x1_x2)
print("\nSomme x1*x3 : ", sum_x1_x3)
print("\nSomme x2*x3 : ", sum_x2_x3)
print("\nVariance x1 : ", var_x1)
print("\nVariance x2 : ", var_x2)
print("\nVariance x3 : ", var_x3)
print("\nVariance y : ", var_y)

print("\nCovariance x1 et y : ", cov_x1_y)
print("\nCovariance x2 et y : ", cov_x2_y)
print("\nCovariance x3 et y : ", cov_x3_y)
print("\nCovariance x1 et x2 : ", cov_x1_x2)
print("\nCovariance x1 et x3 : ", cov_x1_x3)
print("\nCovariance x1 et x4 : ", cov_x1_x4)
print("\nCovariance x2 et x3 : ", cov_x2_x3)
print("\nCovariance x2 et x4 : ", cov_x2_x4)
print("\nCovariance x3 et x4 : ", cov_x3_x4)

print("\nEcart type  x1 : ", ecart_x1)
print("\nEcart type  x2 : ", ecart_x2)
print("\nEcart type  x3 : ", ecart_x3)
print("\nEcart type  x3 : ", ecart_x4)
print("\nEcart type  y : ", ecart_y)

# print("\na = cov(x,y)/var(x) : ", a)
# print("\nb = ya-a*xa : ", b)
# print("\ne = ", e)

print("\nLe coeffiscient de corelation ryx1 = ", ryx1)

print("\nLe coeffiscient de corelation ryx2 = ", ryx2)
print("\nLe coeffiscient de corelation ryx3 = ", ryx3)
print("\nLe coeffiscient de corelation ryx4 = ", ryx4)
print("\nLe coeffiscient de corelation rx1x2 = ", rx1x2)
print("\nLe coeffiscient de corelation rx1x3 = ", rx1x3)
print("\nLe coeffiscient de corelation rx1x4 = ", rx1x4)
print("\nLe coeffiscient de corelation rx2x3 = ", rx2x3)
print("\nLe coeffiscient de corelation rx2x4 = ", rx2x4)
print("\nLe coeffiscient de corelation rx3x4 = ", rx3x4)

y=[1, ryx1, ryx2, ryx3, ryx4]
x1=[ryx1, 1, rx1x2, rx1x3, rx1x4]
x2=[ryx2, rx1x2, 1, rx2x3, rx2x4]
x3=[ryx3, rx1x3, rx2x3,1, rx3x4]
x4=[ryx4, rx1x4, rx2x4,rx3x4, 1]


matrice_r = np.array([y,x1,x2,x3,x4])

print(matrice_r)

det_matrice = mt.determinant_recursive(matrice_r)

matrice_mineur = matrice_r[1:,1:]

print("\nLa matrice mineure : ")
print(matrice_mineur)

det_matrice_mineur = mt.determinant_recursive(matrice_mineur)

print("\nDeterminant D11(matrice mineur) : ", det_matrice_mineur)

D = np.delete(matrice_r, 0, 1)
D = np.delete(D, 0, 0)
print("\nD")
print(D)
D = mt.determinant_recursive(D)
print("\nDeterminant D = ", D)

# print("Determiant avec numpy :", np.linalg.det(D)) 
# the syntax will be M1[row_start:row_end, col_start:col_end] 

D1 = np.delete(matrice_r, 1, 1)
D1 = np.delete(D1, 0, 0)
print("\nD1")
print(D1)
D1 = mt.determinant_recursive(D1)
print("\nDeterminant D1 = ", D1)

# m2
print("Matric r m2")

m2=np.copy(matrice_r)
m3=np.copy(matrice_r)
m4=np.copy(matrice_r)
print(m2)
print("\nM3")
print(m3)

# swaping
m2[:, [0, 2]] = m2[:, [2, 0]]

D2 = m2[1:,1:]
print("\nD2")
print(D2)
D2 = mt.determinant_recursive(D2)
print("\nDeterminant D2 = ", D2)


print("\nM3 before swap")
print(m3)

# swaping
m3[:, [0, 3]] = m3[:, [3, 0]]

print("\nM3 after swap")
print(m3)
D3 = m3[1:,1:]
print("\nD3")
print(D3)
D3 = mt.determinant_recursive(D3)
print("\nDeterminant D3 = ", D3)

# swaping
m4[:, [0, 4]] = m4[:, [4, 0]]

print("\nM4 after swap")
print(m4)
D4 = m4[1:,1:]
print("\nD4")
print(D4)
D4 = mt.determinant_recursive(D4)
print("\nDeterminant D4 = ", D4)


print("D", D)
print("D1", D1)
print("D2", D2)
print("D3", D3)
print("D3", D4)

a_prime = D1/D
b_prime = D2/D
c_prime = D3/D
d_prime = D4/D

a = a_prime*ecart_y/ecart_x1
b = b_prime*ecart_y/ecart_x2
c = c_prime*ecart_y/ecart_x3
d = d_prime*ecart_y/ecart_x4

e = arth_mean_y-(a*arth_mean_x1)-(b*arth_mean_x2)-(c*arth_mean_x3)-(d*arth_mean_x4)

print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
print("e = ", e)

R2 = 1-(det_matrice/det_matrice_mineur)

print("\nR²yx1x2x3x4x = ", R2)




