#Functions basics

# # 3 important featues in a function
# 1. input
# 2.logic
# 3.output

# what is function
# it is a block of code something that resue everytime

# 1.defining a function which is without parameters
def hello():
  print("hello world!")

hello()#calling a function

# 1. input-which is inside braces ()
# 2.logic-print
# 3.output-helloworld!


# 2.defining a function which is with parameters/params
def hello(name):
  print(f"hello {name}")

hello("mamatha")
#f->it is "fstring"(formatted string it is the way to embed expressions inside string literals using curly braces{})
# example
country="india"
capital="New delhi"
print(f"{capital} is the capital of {country}")
# 4.function with return value
#to add  two numbers
def add(a,b):
  return a+b# return keyword store the value in variable when we use return keyword then after we cant access any values
c=add(10,20)
print(c)