import numpy as np
a=input("enter the matrix")
b=input("enter the matrix")
for i in range(0,len(b)):
	a.append(b[i])
print(b)
c=np.append(a,b)
print c

