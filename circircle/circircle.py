#end if

# given points on circle as vectors of a circle 
Q = np.array([3,4])
R = np.array([-4,3])

# given circle parameters 
O = np.zeros(2) #center of circle
r = 5 #LA.norm(Q-O)#radius 


P = np.array([0,-r]) # considering random point on circle

#normal vectors
N1 = norm_vec(P,Q)
#N1 =dir_vec(P,Q)
print(N1)
N2 = norm_vec(P,R)
#N2 = dir_vec(P,R)
print (N2)


#TThe angle between two vectors is given by
#θ = cos−1(#A⊤ B/∥A∥ ∥B∥)
d = np.dot(N1,N2)
#print(d)

n1 = np.sqrt(np.dot(N1,N1))
#print (n1)

n2 = np.sqrt(np.dot(N2,N2))
#print (n2)
#print (d/n1*n2)

teeta = np.arccos(d/(n1*n2)) 

teetadeg = int(np.degrees(teeta)) # angle QOR

print("------------------solution--------------------------------")
print ("Measured the \N{MEASURED ANGLE} QPR of inscribed triangle PQR is = {}\N{DEGREE SIGN}.".format(teetadeg))
print("where P{} is randomly picked point on major Arc".format(P))

print("--------------------------------------------------------------")

########################ploting############

#Input parameters
#Q
#R

#Circle parameters
r = 5
O = np.zeros(2)
P =  np.array(([0,-5])) # imaginary point on circle
#p = np.array(([0,5])) ## inverse triangle point on circle
##Generating the circle
x_circ= circ_gen(O,r)

##Generating all lines
xQR = line_gen(Q,R)

xPR = line_gen(P,R)
xPQ = line_gen(P,Q)



#Plotting all lines
plt.plot(xQR[0,:],xQR[1,:],'-g',label='lineSegmant-QR')
plt.plot(xPR[0,:],xPR[1,:],'--',color="green")
plt.plot(xPQ[0,:],xPQ[1,:],'--',color="green",label='\N{MEASURED ANGLE}QPR = {}$^\circ$'.format(teetadeg))
#plt.plot(xpR[0,:],xpR[1,:],'--',color="purple")
#plt.plot(xpQ[0,:],xpQ[1,:],'--',color="purple",label="QP'R_minorArc= {}deg".format(degPinv))


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
