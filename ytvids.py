import numpy as np
d=np.array([[1,2,3],[1,4,5],[2,4,5]])
print(d)
b=np.array([[2.3,3.0,4.5],[3.5,5.5,6.5]])
print(b)
print(d.ndim)#how many rows that it contains
print(b.ndim)
print(d.shape)#it does to see the rows and coliumns
print(b.shape)
print(d.itemsize)#how much size is there 
print(b.itemsize)
print(d.dtype)#which types of data like integer or float
print(b.dtype)
print(d.size)#how many number of elements are there 
print(b.size)
print(d.nbytes)#it is shortified ver oif d.size*d.itemsize
print(b.size*b.itemsize)
s=np.array([[5,2,3],[9,4,5],[0,4,5]])
print(s[0,2])#so the output shouldf be 3 cause we selected 0 row of 2nd position
print(s[0,:])#so the output should be the 5,2,3 cause we only specified the 0 row
print(s[2,:])#so the output should be 0,4,5 cause we specified 2 row
print(s[:,1])#so output shoukld be 2,4,4 cause we specified 1 column only
s[0,2]=6# we tried to change the second element of 0 row
print(s)