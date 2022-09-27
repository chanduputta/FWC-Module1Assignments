# To find an equation of the line which is perpendicular to the line segment joining the points (1,0) & (2,3) and divides it in the ratio 1:n #

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import subprocess
import shlex


#Given Input vectors
A = np.array([1,0]) 
B = np.array([2,3]) 

#The direction vector of the line joining two points A(1,0), B(2,3) is given by
#M=A−B
M = np.array(A-B)

# position/directional vector of the A&B line segment used as the normal vector of its perpendicular line
print ("Equation of perpendicual line is:")
print(M,"X =", "C")
f  = int(input("enter your required value in 1:n ratio n :  "))  

#The equation of the line perpendicular to line and passing through the point P is given by
#m⊤ (x − P) = 0
u= (2+f)/(1+f)
e= (3)/(1+f)
x = np.array([u,e])
m = M@x       #normal vector m 
print ("Equation of the perpendicual line through point is")
print (m,"X +",k,"= 0")
#The point P that divides the line segment AB in the ratio 1 : k is given by
#P= (B + kA)/(1+k)
