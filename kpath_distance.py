import numpy as np

alat = 1 # it is taken in fraction units


# you need reciprocal matrix below (extract it from scf.out)
f=open("scf.out", "r")
    for line in f:
        if "b(1) =" in line:
            b1 = list(map(float, line.split()[3:6]))
        if "b(2) =" in line:
            b2 = list(map(float, line.split()[3:6]))
        if "b(3) =" in line:
            b3 = list(map(float, line.split()[3:6]))

reciprocal_mat = np.array([b1, b2, b3])


# reciprocal_mat  =  np.array([[1,0,0],[0,1,0],[0,0,1]]) # simple cubic

# You need a text file with kpts in fractional coordinates: only float values are accepted in np.loadtxt
kpts = np.loadtxt("kpts.dat")



cart_kpts =  kpts @ reciprocal_mat

distance = 0.0
print(distance)

for i in range(len(cart_kpts)-1):
    distance += np.sqrt( (cart_kpts[i,0] - cart_kpts[i+1,0])**2 + (cart_kpts[i,1] - cart_kpts[i+1,1])**2  + (cart_kpts[i,2] - cart_kpts[i+1,2])**2 ) 

    print(distance)
