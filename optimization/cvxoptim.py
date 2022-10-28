#Code by Shreyash Chandra, 
#oct 27, 2022
#Released under GNU GPL
#Quadratic program 
#using cvx
import numpy as np
from cvxpy import *
import matplotlib.pyplot as plt 
import sys  #for path to external scripts
sys.path.insert(0,'/home/shreyash/Desktop/matrix/gvv/cbse-papers/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#circle parameters
#P = np.array([3,7]).reshape(2,-1)
V = np.array([[1,0],[0,1]])
u = np.array([0,0]).reshape(2,-1)
d = -1
n= np.array([1,1])

x = Variable((2,1))

#Given function
f =  n@x
obj = Maximize(f)

#Constraints
constraints = [quad_form(x,V) + u.T@x +d <= 0]

#solution
Problem(obj, constraints).solve()

Max_value = f.value

Q = x.value

print("--------------solution-----------------")
print("Maximum value of x+y is {}".format(Max_value) )
print("at point Q({})".format(Q))
#print("x = {} and y = {}".format(x.value[0],x.value[1]))
print("----verified by plot-----------")

############plotting#################

#circle parameters
O =  -u #center of circle -u
r = -d  #.........radius(-f) 
##Generating the circle
x_circ= circ_gen(O.reshape(1,-1),r)
#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='Circle')


#plot the points
#plt.plot(O[0],O[1],'o')
plt.plot(Q[0],Q[1],'o',label='point Q')
#plt.text(Q[0], Q[1])



plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='best')
plt.title('Optimization-Plot')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('/storage/emulated/0/github/cbse-papers/2020/math/10
#solutions/figs/matrix-10-20.pdf')
#subprocess.run(shlex.split("termux-open /storage/emulated/0/github
#school/ncert-vectors/defs/figs/cbse-10-20.pdf"))
#else
plt.show()



