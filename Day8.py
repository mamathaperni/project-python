# #default parameters
# def hello(name):
#     print(f"hello{name}")
# hello(Manasa)  

# 1#
# def hello(name="chandu"):#here at the time of declaration only we are giving some value as defalut so when we call without  paramter also it take values as default.without giving error
#     print(f"hello{name}")
# hello()

# 2# Keyword arguments
# #  two numbers=add them
# def add_numbers(x=10,y=20):#here also we can give the values as default
#     return x+y
# print(add_numbers())    

#scope and global variables
#the function which can able to acess the variables outside the function is called global variable
x=100
def test():
    print(x)
test()#100

def test(y):
    global x
    print(x,y)
test(10)#100 10

# eg2:
n=23
def test(n):
    n=21
    print(n)
test(16)  #21

# Nested function:
# A function inside another function is called nested function.

def hello(name):
    print(f"hello {name}")
def fav_city(city_name,name):
    hello(name)
    print(f"welcome to {city_name}")


fav_city("mumbai","mamatha")
