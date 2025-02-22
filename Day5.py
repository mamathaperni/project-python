#lists
# list always with[]
#we can acess the eleents using index values  eg:items[0]


items=[]#empty list
print(type(items))
1.#creating list
items=["speaker","mic","mobile","laptop"]
print(items[0])#speaker
print(items[3])#laptop

#if we have 100 of items in list and acress the lastone
# so we can use -1  called negative indexing.

print(items[-1])

print(items[-2])

2.#slicing a list
#we can acess the elements using index values
#eg:items[0:3]

print(items[1:3])#['mic', 'mobile']

fruits=["apple","mango","banana","watermelon"]
print(fruits[:3])#['apple', 'mango', 'banana']
print(fruits[0:3])#['apple', 'mango', 'banana']
print(fruits[2:])#['banana', 'watermelon']
print(fruits[3:4])#['watermelon']

3.#modifyting the Listi tems

items=["speaker","mic","mobile","laptop"]
items[3]="pc"#['speaker', 'mic', 'mobile', 'pc']
print(items)

4.#add more items into list

items=["speaker","mic","mobile","laptop"]
items.append("pendrive")
print(items)
items.append("camera")
print(items)

5.#removing elements from the list
# remove method will remove the last element from the list
items.remove("camera")
print(items)#['speaker', 'mic', 'mobile', 'laptop', 'pendrive']

#removing the first element from the list
6.# pop is used to remove the element first and we can also pop by indexing
items.pop(0)
print(items)#['mic', 'mobile', 'laptop', 'pendrive']

7.#removing all elements from the list
items.clear()
print(items)#[]
#clear() will clear all the elements from the list

items=["speaker","mic","mobile","laptop"]
8.#checking for existing ones in the list whether element present in list or not
# eg:to check earbuds in the list

print("earbuds"in items)#False

print("speaker"in items)#True

9.#length of a list
print(len(items))#4

10.#list comprenshion
#it is writing a loop inside the list

scores=[60,70,80,90]
# with list comprension 
L=[i/2 for i in scores]
print(f'data:{L}')#data:[30.0, 35.0, 40.0, 45.0]
#in the above example using list comprension we print the half of the actual value

#with out list compriension
scores=[60,70,80,90]

for i in scores:
 print(i/2)#30.0
35.0
40.0
45.0

