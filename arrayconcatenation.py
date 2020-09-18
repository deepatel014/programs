import numpy as np

a,b,c = map(int,input().split())
arr1 = np.array([input().split() for _ in range(a)],int)
arr2 = np.array([input().split() for _ in range(b)],int)

print(np.concatenate((arr1,arr2),axis=0))
# import numpy

# array_1 = numpy.array([[1,2,3],[0,0,0]])
# array_2 = numpy.array([[0,0,0],[7,8,9]])

# print(numpy.concatenate((array_1, array_2), axis = 1) )