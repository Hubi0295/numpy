import numpy as np
a=np.array([1,2,32000], dtype='int16')
print(a)
b=np.array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
print(b)
print(b.ndim)#get dimenstion

print(b.shape)#get shape

print(a.dtype)#get type

print(a.itemsize)#get size

print(b.dtype)

print(b.itemsize)

print(a.size*a.itemsize)#get total size

print(a.nbytes)#get total size

c=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
print(c[0,:])#get specific row
print(c[:,2])#get specific column
print(c[0,0:6:2])
c[1,5]=20#change specific element
print(c)
c[:,2]=[1,2]#change entire row
print(c)

b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])#3d array
print(b[0,1,1])
print(b[:,1,:])
b[:,1,:]=[[10,20],[30,40]]
print(b)