import random

import numpy as np
base=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
a = np.zeros((2,2,2))
print(a)
b = np.ones((2,2,2),dtype='int8')
print(b)
print(a.nbytes)
print(b.nbytes)

c=np.full((2,2),90)
print(c)

d=np.full_like(base,4)
print(d)

e=np.random.rand(3,3,3)
print(e)
print(e.nbytes)
e=np.random.random_sample(d.shape)
print(e)

f=np.random.randint(10,21, size=(3,3))
print(f)

g=np.identity(5)
print(g)

ala = np.array([[1,2,3]])
repeat = np.repeat(ala,3,axis=0)
print(repeat)

z=np.ones((5,5))
x=np.zeros((3,3))
x[1,1]=9
z[1:-1,1:-1]=x
print(z)
print(x)

#pay attention about copying
a=np.array([1,2,3])
b=a
b[0]=100
print(b)
print(a)
b=a.copy()
b[0]=99
print(b)
print(a)

a = np.array([1,2,3,4])
print(a)
a=a+2
print(a)
a*=2
print(a)

b=np.array([1,0,1,0])
print(np.sin([2*3.141559+1.57075,0,1.57075]))#lol they were right during math lesson
c=a+b
c**=2
print(c)


#algebra
a=np.full((2,3),1)
print(a)
b=np.full((3,2),2)
print(b)
c=np.matmul(a,b)
print(c)

c=np.identity(3)
d=np.linalg.det(c)
print(d)
#statistics
stats = np.array([[1,2,3],[4,5,6]])
print(np.min(stats), np.max(stats))
print(np.min(stats, axis=1))
print(np.sum(stats))

#Reogranizing Arrays
before=np.array([[1,2,3,4],[5,6,7,8]])
after = before.reshape((2,2,2))
print(after)

#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2,v2,v2]))
#horizontal stack
h1=np.ones((2,4))
h2=np.zeros((2,2))
print(np.hstack((h1,h2)))

a=open('text.txt','w')
for x in range(3):
    for x in range(20):
        a.write(str(random.randint(0,127)))
        if x!=19:
            a.write(",")
    a.write("\n")
a.close()
#Miscellaneous
filedata=np.genfromtxt('text.txt',delimiter=',')
filedata=filedata.astype('int8')
print(filedata)

##Boolean masking advanced indexing
x = filedata>100#Thats literally blow my mind
print(x)
a=filedata[filedata>100]
print(a)
c=np.any(filedata>100, axis=0)
print(c)
c=np.all(((filedata>50)&(filedata<100)), axis=0)
print(c)

a = np.array([1,2,3,4,5,6,7,8,9])
b=a[[1,2,8]]
print(b)