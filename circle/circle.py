#Code by Shreyash Chandra (works on termux)
#October 11, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the angle |_QPR of thriangle inscribed in the circle x2 + y2 = 25 if Q and R coordinates are (3,4) & (-4,3) respectively . 


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
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
O = np.zeros(2)
N1 = norm_vec(O,Q)
#print(N1)
N2 = norm_vec(O,R)
#print (N2)


#TThe angle between two vectors is given by
#θ = cos−1(#A⊤ B/∥A∥ ∥B∥)
d = np.dot(N1,N2)
#print(d)

q = np.sqrt(np.dot(Q,Q))
#print (q)

r = np.sqrt(np.dot(R,R))
#print (r)
#print (d/q*r)

teeta = np.arccos(d/(q*r))

teetadeg = np.degrees(teeta)
#print( teetadeg)

degP = teetadeg/2
print("------------------solution--------------------------------")
print ("Angle QPR of given triangle is :",int(degP),"degrees.")
print("--------------------------------------------------------------")

########################ploting############

#Input parameters
Q =  np.array(([-4,3])) #given vector
R =  np.array(([3,4])) #given vector

#Circle parameters
r = 5
O = np.zeros(2)
P =  np.array(([0,-5])) # imaginary point on circle
##Generating the circle
x_circ= circ_gen(O,r)

##Generating all lines
xQR = line_gen(Q,R)
xOR = line_gen(O,R)
xOQ = line_gen(O,Q)
xPR = line_gen(P,Q)
xPQ = line_gen(P,R)


#Plotting all lines
plt.plot(xQR[0,:],xQR[1,:],label='givenChord')
plt.plot(xOR[0,:],xOR[1,:],"r-")
plt.plot(xOQ[0,:],xOQ[1,:],"r-",label='QOR = 90deg')
plt.plot(xPR[0,:],xPR[1,:],'-.',color="green")
plt.plot(xPQ[0,:],xPQ[1,:],'-.',color="green",label='QPR = 45deg')



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
plt.grid() # minor
plt.axis('equal')


#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-20.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/#school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
plt.show()


