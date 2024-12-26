d1={"a":1,"b":2,"c":3,"d":4}
d2={"a":100,"b":200,"c":300,"d":400}

for i in d1:
    d2[i]=d2.get(i,0)+d1[i]
print(d2)

final=dict(sorted(d2.items(),key=lambda i:i[1],reverse=True))
print(final)