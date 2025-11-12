
import numpy as np

alat = 1 # it is taken in fraction units


# there are three inputs needed for this script: 


# 1. provide reciprocal matrix from scf.out here
reciprocal_mat  =  np.array([[1,0,0],[0,1,0],[0,0,1]]) # simple cubic

# 2. provide a text file readable by numpy; which is a list of kpoints (sample file is contained in the main directory)
kpts = np.loadtxt("kpts.dat")

# 3. provide high symmetry path, along which you want the path
high_sym = ['G', 'X', 'M','G', 'R', 'X', 'R', 'M']

cart_kpts =  kpts @ reciprocal_mat

distance = [0]

dist=0
for i in range(len(cart_kpts)-1):
    dist += np.sqrt( (cart_kpts[i,0] - cart_kpts[i+1,0])**2 + (cart_kpts[i,1] - cart_kpts[i+1,1])**2  + (cart_kpts[i,2] - cart_kpts[i+1,2])**2 ) 

    distance.append(dist)

 


 

coord=distance

 
 

for i in range(0,len(high_sym)):
      print('set label ' + "'" + str(high_sym[i]) + "'" + ' at ' + str(coord[i]) + ' , -2.06 center font ' + " 'Times bold,25' ")
      print('set arrow from ' + str(coord[i]) + ' ,graph 0 to '+ str(coord[i]) + ' , graph 1 as 1')

 
