#Dictionaries

#Dictionary has both key and value pair.

#creating a Dictionary

# student={}->empty dictionary

#how to store values in dictionary
student={"name":"manasa","age":20,"gender":"female" ,"qualified":False}
print(student)
#key and value are linked using :


#2. Accessing values:
print(student["name"])

#3.how to modify particular name
student["name"]="mamatha"
print(student)

#4 looping through a Dictionary
print(student)
for key in student:#here we acess keys
    print(key)

for value in student.values():
    print(value)#here we acess values

#to print both key and value together
for k,v in student.items():
    print(k,v)#here items used to acess both key and value together.

 #   to check particular value or key is present or not in dictionaries
for k in student:
    if k=="name":
        print("key is present")

        # or we can write simply

if "name" in student:
    print(True)
else:
    print("False")      

