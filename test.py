import numpy as np
from scipy.cluster import vq
from matplotlib import pyplot as plt

x = np.random.randint(25,50,(25,2))
y = np.random.randint(60,90,(25,2))
z = np.vstack((x,y))
#z = z.reshape((50,1))
print z

plt.scatter(z[:,0],z[:,1]),plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()
#plt.hist(z,256 ,[0,256])
#plt.show()

#centers,dist = vq.kmeans(z,2)
#print centers

#plt.hist(z,256,[0,256]),plt.show()
#code, distance = vq.vq(z,centers)
#a = z[code==0]
#b = z[code==1]
#print "a\n"+str(a)+"\nb\n"+str(b)

#plt.hist(a,256,[0,256],color = 'r')
#plt.hist(b,256,[0,256],color = 'b')
#plt.hist(centers,32,[0,256],color = 'y')
#plt.show()

