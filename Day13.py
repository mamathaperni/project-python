#list[,]
#tuple(,)
#dict{key:value}
#set{,}
#creating a Tuple:
my_tuple=(1,2,3)
print(my_tuple)

#Acessing tuple elements
#based on indexing we can acess the values
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

#Tuple operations:
#how to combine 2 tuples:
tp1=(1,2,3)
tp2=("hai","hlo","hey")
print(tp1+tp2)

print(tp1*5)#Here the values are repeating 5 times
#if we want to multiply  a number using tuple multiple times
tup3=(416,)
print(tup3*20)

#Tuple unpacking:
a,b,c=(10,20,30)# here we are assiging or unpacking values to a variable
print(a)
print(b)
print(c)

#once you create a tuple we cannot modify. where it is immutable

#list vs Tuple
#list is mutable and it is like a train where we can do a lot of modifications
#tuple is immutable and it is like a bus where we cannot do any modifications
#list is memory high
#tuple is memory low


#sets
#set is a collection of unique elements
#it is mutable
#it is unordered

l=[1,2,3,4,2,12,2,2,4]#here set will print unique values
print(set(l))
print(type(l))#<class 'list'>
print(type(set(l)))#<class 'set'>

#set oprations
s1={1,2,3,4,5,6}
s2={1,2,3,8,9}
print(s1.union(s2))#it will print all the values from both sets which are unique and repeated values are not printed
#{1, 2, 3, 4, 5, 6, 8, 9}
print(s1.intersection(s2))#it will print common values from both sets
#{1, 2, 3}

print(s1.difference(s2))#it will print the values which are not common in s1
print(s2.difference(s1))#it will print the values which are not common in s2