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
C = n@A
### distance betwwen (0,0) and line nX=c is |c| / ||n|| ####
k = np.linalg.norm(n)

d = abs(C)/k

print (d)

angle = np.arcsin(d/5) + np.arcsin(d/5)

theeta = np.degrees(angle/2)

print ("required angle QPR is ~",theeta)

########################ploting############

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#Generating points on a circular arc
def circ_arc(O,r,theta1,theta2,len):
	theta = np.linspace(theta1,theta2,len)*np.pi/180
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
	

plt.plot(A,B)
#plt.show()
