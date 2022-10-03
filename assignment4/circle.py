# circle assignment
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import math
#Orthogonal matrix
omat = np.array([[0,1],[-1,0]]) 
def dir_vec(A,B): ##dirction vector
  return B-A

def norm_vec(A,B):  ##normal vector
  return np.matmul(omat, dir_vec(A,B))
  
A = np.array(([3,4]))
B = np.array(([-4,3]))

n = norm_vec(A,B)
c = n@A
##distance betwwen (0,0) and line nX=c####
k = np.linalg.norm(n)

d = c/k

print (d)

angle = np.arcsin(d/5)
theeta = np.degrees(angle)

print ("required angle QPR is ~",theeta)
plt.plot(A,B)
#plt.show()
