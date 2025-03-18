#python Modules
#eg modules: math,random
#  to communicate with modules we use import keyword

# import math
#python library/python module

# it means python has collected all information about math module and it is ready to use.

import math
print(math.sqrt(100))#10.0 

print(math.pi)#3.141592653589793

print(math.pow(2,10))#1024.0

print(math.factorial(5))#120

import math as m #we no need to use math every time we can use m.
print(m.pow(2,4))#16.0

import random

print(random.random())#0.8411840456375558

print(random.randint(10,1000))# it is better in case of otp in general purpose.

list1=["blue","green","pink"]
print(random.choice(list1))# it will give random color every time.
print(random.shuffle(list1))
print(list1)#['green', 'blue', 'pink'] vales after shuffeling.
# it is used  in gamming where we can shuffle the values every time
# it is used in quiz where we can shuffle the questions every time.

list2=["c1","c2","c3","c4","c5","c6","c7","c8"]
print(random.shuffle(list2))
print(list2)#['c7', 'c2', 'c4', 'c3', 'c5', 'c1', 'c6', 'c8']


# python libararies-os,json,requests.