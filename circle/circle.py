#Code by Shreyash Chandra (works on termux)
#October 25s, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the angle |_QPR of thriangle inscribed in the circle x2 + y2 = 25 if Q and R coordinates are (3,4) & (-4,3) respectively . 


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
from math import *
import sys  #for path to external scripts
sys.path.insert(0,'/home/shreyash/Desktop/matrix/gvv/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
#import subprocess
#import shlex
#end if


# given points on coordinates as vectors
Q = np.array([3,4])
R = np.array([-4,3])

#Circle parameters from given eqn --> X^T X + 2u^T X + f  = 0
u = -np.zeros(2)
f = -25

#we get
O =  -u #center of circle
r = int(np.sqrt(np.dot(u,u)-f))  #LA.norm(Q-O) .........radius(-f) 

# To take random point on circle
n = int(input("Input an angle alpha[0 to 360] to generate a point on circle:"))#99
alpha = np.radians(n)
#print(alpha,"alpha")
x =r*np.cos(alpha)
y=r*np.sin(alpha)
P = np.array([x,y])
#print(P,"random point P")
check = np.linalg.norm(P)
#print(check,"= 5 or not")
N1 = dir_vec(P,Q)
#print(N1,"norm_vec1")
N2 = dir_vec(P,R)
#print (N2,"norm_vec2")

#The angle between two vectors is given by
#θ = cos^−1(#A^⊤B/∥A∥ ∥B∥)

d = np.dot(N1,N2)
n1 = np.linalg.norm(N1)
n2 = np.linalg.norm(N2)
teeta = np.arccos(d/(n1*n2))

degP = int(np.degrees(teeta)) # angle QPR


print("------------------solution--------------------------------")
print ("Measured the \N{MEASURED ANGLE} QPR of inscribed triangle PQR is = {}\N{DEGREE SIGN}.".format(degP))
print("where vertex P is {} on circle".format(P))
print("--------------------------------------------------------------")

########################ploting############

##Generating the circle
x_circ= circ_gen(O,r)

##Generating all lines
xQR = line_gen(Q,R)
xPR = line_gen(P,R)
xPQ = line_gen(P,Q)

#Plotting all lines
plt.plot(xQR[0,:],xQR[1,:],'--',color="green",label='side QR')
plt.plot(xPR[0,:],xPR[1,:],color="green")
plt.plot(xPQ[0,:],xPQ[1,:],color="green",label='\N{MEASURED ANGLE}QPR = {}$^\circ$'.format(degP))


#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')


#Labeling the coordinates
tri_coords = np.vstack((O,Q,R,P)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','Q','R','P']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the txt
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.title('plot of an inscribed triangle PQR')
plt.grid() # minor
plt.axis('equal')


#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-20.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/#school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
plt.show()


