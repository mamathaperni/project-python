# let say we have a list L1=[1,2,2,3,2,3,4,5],now  identify the most repetavive element in the list.
#1s-1
#2s-3
#3s-2
#4s-1
#5s-1
num_counter={}
L1=[1,2,2,3,2,3,4,5]
for i in L1:
    if i in num_counter:

        num_counter[i] +=1
    else:
        num_counter[i]=1
print(num_counter)#{1: 1, 2: 3, 3: 2, 4: 1, 5: 1}

#how to identify the higihest
temp=0
final_result=None
for k,v in num_counter. items():
 print(f"k:{k},v:{v},temp:{temp}")
 if v>temp:
    temp=v
    final_result=k
#k:1,v:1,temp:0
# k:2,v:3,temp:1
# k:3,v:2,temp:3
# k:4,v:1,temp:3
# k:5,v:1,temp:3