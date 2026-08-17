# basics of numpy

import numpy as np

list1 = [1.1,2.2,3.3,4.4]
print(type(list1),'\n',list1,'\n')

arr1 = np.array(list1)

print(type(arr1),"\n")
print(arr1)
print()
tup1 = (1.1,2.2,3.3,4.4)
print(type(tup1),"\n")
print(tup1)
arr2 = np.array(tup1)

print(type(tup1),"\n")

print(tup1)

arr3 = np.array([list1,tup1,arr2])
print(type(arr3),"\n")

print(arr3)