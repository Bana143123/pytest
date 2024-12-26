l1=[1,2,3,4,5]
l2=[6,7,4,5,8]

com=[]
for i in l1:
    if i in l2:
        com.append(i)

print(com) 

#Another way

d = list(set(l1) & set(l2))
print(d)
