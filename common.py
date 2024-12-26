l1=[1,2,3,4,5]
l2=[6,7,8,9,5,4]
res=[]
for i in l2:
    if i in l1:
        res.append(i)
print(res)
l3=l1+l2
print(l3)
i=0
while i<len(l3):
    j=i+1
    while j<len(l3):
        if l3[i]==l3[j]:
            l3.pop(j)
        else:
            j+=1
    i+=1
print(l3)
final=[]
for i in range(len(l3)):
    for j in range(i+1,len(l3)):
        if l3[j]*l3[i] == 10: #and ((l3[i],l3[j]) or (l3[j],l3[i])) not in final:
            final.append((l3[j],l3[i]))
print(final)

