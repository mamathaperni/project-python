# Basic Error Handling:
#handling of errors is called error handling

# types of errors:
# 1.syntaxError 

# print("hello world"
#    print("hello world"
#          ^
# SyntaxError: '(' was never closed

#2.Type Error
# a=2
# b="hello"
# print(a+"hello")#TypeError: unsupported operand type(s) for +: 'int' and 'str'
# it is not going to add 2 different datatypes


#3 nameError
# m
#   we are not declaring with any value so it gives error called name error
# NameError: name 'm' is not defined


#4 IndexError
# list=[1,2,3,4,5]
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])
# print(list[5])
# print(list[5])
          
# IndexError: list index out of range
# because we print the values according to index rather than the range of index we cant able to print the values 

#5 KeyError
# d1={'k1':'v2'}
# print(d1['k1'])
# print(d1['k2'])
#     print(d1['k2'])
          
# KeyError: 'k2'
# the keys which are not defined we cant able to access it

#6 valueError
# a=int(2.3)
# print(a)

# a=int("hello")#we cant able to convert string to an integer 
# and it gives valueError
# print(a)
# ValueError: invalid literal for int() with base 10: 'hello'


#zero divisionError
# a=10/0
# print(a)
#     a=10/0
      
# ZeroDivisionError: division by zero

# we can handleErrors in python using try and except
# try:
#     result=10/0
# except ZeroDivisionError:
#     print("you are not able to divide by zero") #you are not able to divide by zero   
    # here it is meaningful to print the error message so that  user can easily understand

# try:
#     a=int("hello")
# except ValueError:
#     print("it cant covert string into integer")#it cant covert string into integer

    # if you handle the error your code will continue and work
    # if you not continue the errors the code will stop there itself
try:
    a=int("hello")
except ValueError:
    print("it cant covert string into integer")
y=2+3
print(y)#5
# even though it gives error and contine the code  by using Errorhandling