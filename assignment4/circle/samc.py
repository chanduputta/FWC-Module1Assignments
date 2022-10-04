
#To find the angle |_QPR formed by the triangle PQR which in inscribed in circle given point Q R given.


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import subprocess
import shlex


#Input vectors
Q = np.array([3,4])
R = np.array([-4,3])
#R = np.array([2,2])
i = np.array([Q,R])
p = np.linalg.inv(i)
q = np.array([1,1])
n = p@q         #normal vector n

M = np.array(Q-R)
dist = np.linalg.norm(M)
print("distance is",dist)

print("Equation of line is")
print(n,"X =", "1")
k = np.linalg.norm(n)
print("norm of line nT ", k)
d =1/k
print("distance from origin ", d)  #dist from origin to line = |c|/||n||
theeta = np.arcsin(d/5)
print("angle |_QPR =",theeta)


