#Numpy  (numerical python)

#importing numpy

import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)#[1 2 3 4 5]

#adding couple of arrays
arr1=np.array([1,2,3,4])
arr2=np.array([6,7,3,4])
print(arr1 + arr2)#[7 9 6 8]


# accesing each element using index
arr3=np.array([1,2,3,4,5,6])
print(arr3[0])#1
print(arr3[1])#2
print(arr3[-1])#6
print(arr3[-3])#4
# accessing each element using index and slicing
print(arr3[0:2])#[1 2]
print(arr[0:3])#[1 2 3]



#numpy allows to create matrices
#  we can able to reshape it

arr=np.array([1,2,3,4,5,6,])
print (arr.shape)#(6,) it is 6,1 matrix
# to reshape it
print(arr.reshape(2,3))
# [[1 2 3]
#  [4 5 6]]

#numpy also used to read images  because images are nothing but RGb values

# broadcast- where we can apply the opereation at once to each and every element 

arr=np.array([1,2,3,4,5,6,])
print(arr+1) #[2 3 4 5 6 7] it add one to each and every element.
print(arr+6) #[7 8 9 10 11 12] it add 6 to each and every element.

# broadcast is used in dot(.) products

m1= np.array([[1,2],[3,4]])
m2=np.array([[5,6],[7,8]])
print (m1.dot(m2))
# [19 22]
#  [43 50]]

# For 2x2 matrices, the result is:
# [[(1×5 + 2×7)  (1×6 + 2×8)],
#  [(3×5 + 4×7)  (3×6 + 4×8)]]
# Let's break down each element:

# Top left: (1×5) + (2×7) = 5 + 14 = 19
# Top right: (1×6) + (2×8) = 6 + 16 = 22
# Bottom left: (3×5) + (4×7) = 15 + 28 = 43
# Bottom right: (3×6) + (4×8) = 18 + 32 = 50

#simple  statical calculations
print(np.mean(arr)) #3.5
# Sum of elements: 1 + 2 + 3 + 4 + 5 + 6 = 21
# Number of elements: 6
# Mean = 21/6 = 3.5

#to get standard deviasion
print(np.std(arr)) #1.707825127659933

#to generate random numbes using numpy
print(np.random.rand(6)) # [0.96511283 0.03134909 0.09197334 0.09419635 0.19450173 0.69383794]

#if we have some missing data.
arr4=[1,2,3,np. nan,5,6]
print( np.isnan(arr4)) #[False False False  True False False]

import time
 
 #using list
L1= list(range(10000000))
start=time.time()
sum(L1)
end=time.time()
print(end-start) #0.2502562999725342

L1=np.array(L1)
start=time.time()
np.sum(L1)
end=time.time()
print(end-start) # 0.006913661956787109
