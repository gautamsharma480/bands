import numpy as np

alat = 1 # it is taken in fraction units

reciprocal_mat  =  np.array([[1,0,0],[0,1,0],[0,0,1]]) # simple cubic

kpts = np.loadtxt("kpts.dat")



cart_kpts =  kpts @ reciprocal_mat

distance = 0.0
print(distance)

for i in range(len(cart_kpts)-1):
    distance += np.sqrt( (cart_kpts[i,0] - cart_kpts[i+1,0])**2 + (cart_kpts[i,1] - cart_kpts[i+1,1])**2  + (cart_kpts[i,2] - cart_kpts[i+1,2])**2 ) 

    print(distance)
