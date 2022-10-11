#Code by Shreyash Chandra (works on termux)
#October 10, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the equation of line which is perpenducular to line segment joining the points (1,0) & (2,3) divides it in the ratio 1:n . 


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
from math import *
import sys                                          #for path to external scripts
sys.path.insert(0,'/home/shreyash/Desktop/matrix/gvv/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if
 
# given points on coordinates as vectors
A = np.array([1,0])
B = np.array([2,3])

N = norm_vec(A,B)

#direction vector of line joining 2 given points is
M = dir_vec(A,B)

# position/directional vector of the A&B line segment used as the normal vector of its perpendicular line

#The point P that divides the line segment AB in the ratio 1 : n is given by#P= (B + nA)/(1+n)
n  = int(input("enter your required n for 1:n ratio (n>=0) :  ")) 
u= (2+n)/(1+n)   
e= (3)/(1+n)   
p = np.array([u,e]) #abtained point P by section formula in 1:n ratio 
#print (p,"point ofint")


#The equation of the line perpendicular to #n⊤ (x) = C and passing through the point P is given by "m⊤ (x − P) = 0"
C = M@p       #Constant C 
print("---------------------------------------------")
print ("Equation of perpendicular line dividing given line-segment in 1 :",n,"ratio is:")
print(M,"X =", C)
print ("-----------------------------------------------")
##plot#######################
#Input parameters
a = np.array((N,M))

b = (([3,((2+n)/(1+n)+((9/(1+n))))]))

e1 = np.array(([1,0])) # standard basic vector
n1 = a[0,]
n2 = a[1,]
c1 = b[0]
c2 = b[1]

#O =  np.array(([1,-1]))
#Solution vector

#r = 7
#Direction vectors
m1 = omat@n1
m2 = omat@n2

#Points on the lines
x1 = c1/(n1@e1)
A1 =  x1*e1
x2 = c2/(n2@e1)
A2 =  x2*e1


#Generating all lines
k1=-3
k2=0
x_AB = line_gen(A,B)

x_CD = line_dir_pt(m2,A2,k1,k2)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='Given line-segment')
plt.plot(x_CD[0,:],x_CD[1,:],label='{}X={}'.format(M,C) )

#Labeling the coordinates
tri_coords = np.vstack((A,B,p)).T
#tri_coords = p.T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
#plt.scatter(tri_coords[0], tri_coords[1])
vert_labels = [A,B,p]
#plt.plot(x_circ[0,:],x_circ[1,:],label='x^2+y^2−2x+2y=47')
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-7.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/school/ncert-vectors/defs/figs/cbse-10-7.pdf"))
#else
plt.show()
