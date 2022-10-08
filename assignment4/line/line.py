#To Find line equation which is perpendicular to the line segment joining the points (1,0) & (2,3) and divides it in the ratio 1:n #

#Python libraries for math and graphics
import numpy as np                        
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math                                 
import subprocess                           
import shlex
                                            
#local import
#Orthogonal matrix                          
omat = np.array([[0,1],[-1,0]])

#Rotation Matrix                            
def rot(theta):                                 
c = np.cos(theta)
    s = np.sin(theta)                           
return  np.array([[c,-s],[s,c]])        

#from line.funcs import *
def dir_vec(A,B):                             
return B-A

def norm_vec(A,B):                            
return np.matmul(omat, dir_vec(A,B))


#Given Input vectors
A = np.array([1,0])
B = np.array([2,3])
                                            
#The direction vector of the line joining two points A(1,0), B(2,3) is given by         
#M=A−B
M = dir_vec(A,B)
                                            
# position/directional vector of the A&B line segment used as the normal vector of its perpendicular line
print ("Equation of perpendicular line is:")
print(M,"X =", "C")
n  = int(input("enter your required value in 1:n ratio n (n>=0) :  "))                                                              #The point P that divides the line segment AB in the ratio 1 : k is given by
#P = (B + kA)/(1+k)                         
u= (2+n)/(1+n)                              
v= (3)/(1+n)                                
P = np.array([u,v])                         
#The equation of the line perpendicular to line and passing through the point P is given by 
#m⊤ (x − P) = 0 or #mTx-mTP = 0
c = M@P       # mT.P
print ("Equation of the perpendicular line through point is")
print (M,"X =",c) #required line equation
#######################################################
#
#To plot

from math import *
#import sys    #for path to external scripts
#sys.path.insert(0,'/cd ../cd ../CoordGeo')     #path to my scripts
#local imports
#Generate line points                       
def line_gen(A,B):
  len =10                                     
  dim = A.shape[0]                            
  x_AB = np.zeros((dim,len))                  
  lam_1 = np.linspace(0,1,len)                
  for i in range(len):
      temp1 = A + lam_1[i]*(B-A)                  
      x_AB[:,i]= temp1.T
    return x_AB                               
#                                           
def line_dir_pt(m,A,k1,k2):
  len = 10                                    
dim = A.shape[0]                            
x_AB = np.zeros((dim,len))                  
lam_1 = np.linspace(k1,k2,len)
for i in range(len):                          
    temp1 = A + lam_1[i]*m                      
    x_AB[:,i]= temp1.T                        
   return x_AB

#from triangle.funcs import *               
#from conics.funcs import circ_gen

#Input parameters                           
A = np.array(([3,-1],[1,3])) #vectors of two
 lines
B = np.array(([3,((2+n)/(1+n)+((9/(1+n))))])
)
e1 = np.array(([1,0]))
n1 = A[0,:]                                 
n2 = A[1,:]
c1 = B[0]                                   
c2 = B[1]

O =  np.array(([1,-1]))
#Solution vector
x = LA.solve(A,B)                           
r = 7                                       
#Direction vectors                          
m1 = omat@n1
m2 = omat@n2
                                            
#Points on the lines
x1 = c1/(n1@e1)                             
A1 =  x1*e1
x2 = c2/(n2@e1)
A2 =  x2*e1

#print(x)
#x_circ= circ_gen(O,r)                      
#Generating all lines                       
k1=3
k2=-3
x_AB = line_dir_pt(m1,A1,k1,k2)

x_CD = line_dir_pt(m2,A2,k1,k2)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='given line-1')
plt.plot(x_CD[0,:],x_CD[1,:],label='perpenducular line-2 ')

#Labeling the coordinates
#tri_coords = np.vstack((x)).T
tri_coords = x.T                            
#plt.scatter(tri_coords[0,:], tri_coords[1,:]) 
        plt.scatter(tri_coords[0], tri_coords[1])
vert_labels = ['intersecting point']
#plt.plot(x_circ[0,:],x_circ[1,:],label='x^2+y^2−2x+2y=47')
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0], tri_coords[1]), # this is the point to label                            textcoords="offset points", # how to position the text
                 xytext=(-5,5), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
                                           
#if using termux
plt.savefig('/sdcard/download/python/line/figure.pdf')
subprocess.run(shlex.split("termux-open  /sdcard/download/python/line/figure.pdf"))
#else
#plt.show()                                                                     
