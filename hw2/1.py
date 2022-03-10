import m
import numpy
from numpy import linalg as LA
import time
import random

a =random.randint(1, 10)
b =random.randint(1, 10)
matrix = [[] for i in range(a)]


def copy_matrix(matrix):
    m1 = [ [] for i in range(len(matrix))]
    for i in range(len(matrix)):
        m1[i] = matrix[i][:]
    return m1
    
for i in matrix:
    for j in range(b):
        i.append(random.randint(-10, 10))
print(a,b)
time1_m = time.perf_counter()
m.square_matrix(copy_matrix(matrix))
time1_m=time.perf_counter() - time1_m
time1_n = time.perf_counter()
numpy.power(copy_matrix(matrix),2)
time1_n = time.perf_counter() - time1_n
print(time1_m,time1_n)

time2_m = time.perf_counter()
m.transport_matrix(copy_matrix(matrix))
time2_m=time.perf_counter() - time2_m
time2_n = time.perf_counter()
g = numpy.array(copy_matrix(matrix))
g = g.transpose()
time2_n=time.perf_counter() - time2_n
print(time2_m,time2_n)

time3_m = time.perf_counter()
m.det(copy_matrix(matrix),a,b)
time3_m = time.perf_counter() - time3_m
time3_n = time.perf_counter()
if a == b:
    h = LA.det(copy_matrix(matrix))
time3_n = time.perf_counter() - time3_n
print(time3_m,time3_n)
