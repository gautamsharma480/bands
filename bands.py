f_pw=open('bands.out','r')

 

high_sym = ['X', 'M', 'R','X']

 

coord=[]
for line in f_pw:
        if 'high-symmetry' in line:
                k_length = float(line.split()[7])
                #print(k_length)
                coord.append(float(k_length))

 

#print(coord)
#print(high_sym)

 

for i in range(0,len(high_sym)):
      print('set label ' + "'" + str(high_sym[i]) + "'" + ' at ' + str(coord[i]) + ' , -2.06 center font ' + " 'Times bold,25' ")
      print('set arrow from ' + str(coord[i]) + ' ,graph 0 to '+ str(coord[i]) + ' , graph 1 as 1')

 

 

f_pw.close()

