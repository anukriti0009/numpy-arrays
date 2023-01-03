#-*- coding: utf-8 -*-
import numpy as np 
x = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])
x.flatten()
print(x)


a1 = x.flatten()
a1[0] = 99
print(x)

print(a1)


a2 = x.ravel()
a2[0] = 98
print(x)








