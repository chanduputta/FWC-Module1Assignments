#To find the equation of a line which passes through given line_segment perpendicually in 1:n ratio 

#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
#import subprocess
#import shlex
import sys # for path external script


#Given Input vectors
A = np.array([1,0]) 
B = np.array([2,3]) 

#The direction vector of the line joining two points A(1,0) & B(2,3) is given by "M=A−B"
M = np.array(A-B)

# position/directional vector of the A&B line segment used as the normal vector of its perpendicular line
print ("Equation of perpendicular line is:")
print(M,"X =", "C")
n  = int(input("enter your required n for 1:n ratio (n>=0) :  "))  

#The equation of the line perpendicular to #n⊤ (x) = C and passing through the point P is given by "m⊤ (x − P) = 0"
#The point P that divides the line segment AB in the ratio 1 : n is given by#P= (B + nA)/(1+n)
u= (2+n)/(1+n)   
e= (3)/(1+n)   
p = np.array([u,e]) #abtained point P by section formula in 1:n ratio 
C = M@p       #Constant C 
print ("Equation of the perpendicual line through 1 :",n,"rato is:")
print (M,"X =",C)


#########################################################################


####plotting part####

#x1 = C/
def line_gen(A,B):
   len =np.sqrt(10)
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB



#Given points
A = np.array([1,0])
B = np.array([2,3])
#R = np.array(([2+n,2]))


x_AB = line_gen(A,B)
#x_PR = line_gen(P,R)
#x_QR = line_gen(Q,R)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$AB$')
#plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
#plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')

#Labeling the coordinates
#tri_coords = np.vstack((P,Q,R)).T
#plt.scatter(tri_coords[0,:], tri_coords[1,:])
#vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.title('equation of straight line')
#plt.savefig('/sdcard/download/iith/python/Assignment-4/figure.pdf')  
#subprocess.run(shlex.split("termux-open /sdcard/download/iith/python/Assignment-4/figure.pdf"))
plt.show()
