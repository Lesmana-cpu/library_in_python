import numpy as np
a1 = np.array([1,3])
b1 = np.array([2,1])

# perkalian dot
c1 = np.dot(a1,b1)
print(c1)

# perkalian cross
a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2,b2)
c2o = np.cross(b2,a2)
print(c2)
print(c2o)