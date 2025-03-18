# Q1. Lets say we have a list L1 = [1, 2, 2, 3, 2, 3, 4, 5], now identify the most repetitive element in the list?

num_counter1={}
L=[1,2,2,3,2,3,4,5]
for i in  L:
    if i in num_counter1:
        num_counter1[i]+=1
    else:
        num_counter1[i]=1
print(num_counter1)

#to identify most repetative element
temp=0
result=None
for k,v in num_counter1.items():
 print(f"k:{k},v:{v},temp:{temp}")   
if v>temp:
    temp=v
    result=k

