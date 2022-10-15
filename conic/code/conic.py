#Code by Shreyash Chandra (works on termux)
#October 15, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To find the locus of mid point of PQ where P is (1,0) and Q is a point on the locus y**2 = 8*x --eqn 


#Python libraries for math and graphics
import numpy as np
from sympy import Symbol,solve,diff
import matplotlib.pyplot as plt
from numpy import linalg as LA
from math import *
import sys                                          #for path to external scripts
sys.path.insert(0,'/home/shreyash/Desktop/matrix/gvv/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import conic_quad

#equation of conic formula
#y**2 = 8*x ------given locus eqn

#Input parameters from given eqn

V = np.array(([0,0],[0,1]))
#print(V)
u = np.array([-4,0])
#print(u)
f = 0 


#given point
P = np.array([1,0])


#symbols
x = Symbol('x')
y = Symbol('y')
X=np.array([x,y])
#print (X)

#section formula for 1:1 
#X = (Q+P)/2
Q = 2*X - P
#print(Q)

q_locus = conic_quad(X,V,u,f)	# given locus
x_locus = conic_quad(Q,V,u,f)   # obtained/req locus
print("------------------------------------------------")
print(q_locus,"= 0 --> given locus")
print(x_locus/4,"= 0 --> req locus")
print("------------------------------------------------")

########################ploting############
#parameters
Q = np.zeros(2)
X = (Q+P)/2

#generate the locus
y = np.linspace(-4, 4, 500)
x = ((y ** 2)+2)/4
k = np.linspace(-5, 5, 50000)
h = (k ** 2)/8
#generate line
x_QP = line_gen(Q,P)
#plotting the locus
plt.plot(h, k, label= "{}=0 given eq".format(q_locus))
plt.plot(x, y, label= "{}=0 msrd eq".format(x_locus/4))
#plot line
plt.plot(x_QP[0,:],x_QP[1,:])
#Labeling the coordinates
tri_coords = np.vstack((P,X,Q)).T
plt.scatter(tri_coords[0, :], tri_coords[1, :])
vert_labels = ['P','X','Q']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
                 (tri_coords[0, i], tri_coords[1, i]),
                 textcoords="offset points",
                 xytext=(0, 10),
                 ha='center')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Found the locus')
    plt.legend(loc='best')
    plt.grid()
    plt.axis('equal')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10/solutions/figs/matrix-10-20.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github/#school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
plt.show()
