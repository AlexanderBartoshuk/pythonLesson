import numpy as np
from numpy import pi

a = np.arange(15).reshape(5,3)
print(a)
print(a.shape)

b = np.array([6,7,8])
print(b)

c = np.array([(1,2,3),(5,6,7)])
print(c)

d = np.empty((2,3))
print(d)


np.linspace(0,2,9)
x = np.linspace(0.2 * pi,100)
f = np.sin(x)
print(f)

print(np.arange(1000).reshape(10,100))

c = np.arange(24).reshape(2,3,4)
print(c)

a = np.array([20,30,40,50])
b= np.arange(4)
c = a - b
print(c)


rg = np.random.default_rng(1)
a = np.ones((2,3), dtype=int)
b = rg.random((2,3))
a *=3 
print(a)
b += a
print(b)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi,3)
print(b.dtype.name)
c = a+b
print(c)


# Universal functions