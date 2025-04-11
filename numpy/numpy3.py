import numpy as np
rg = np.random.default_rng(1)

def f(x,y):
    return 10 * x + y

b = np.fromfunction(f,(5,4), dtype=int)
print(b)
print(b[2,3])
print(b[0:5,2])

c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
               [ 10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
print(c.shape)

for element in b.flat:
    print(element)

a = np.floor(10 * rg.random(3,4))
print(a)