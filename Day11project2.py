def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def mult(a,b):
    return a*b
 

def div(a,b):
    return a/b

def calculator():
    print("selet operation")
    print("1.add")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    choice=input("enter choice :")
    if choice in('1','2','3','4'):
        num1=float(input("enter first number"))
        num2=float(input("enter second number"))
        if choice =='1':
            print(num1+num2)
        elif choice == '2':
               print(num1-num2)
        elif choice == '3':
            print(num1*num2)
        elif choice == '4':
            print(num1/num2)
        else:
            print("invalid input")
            
calculator()