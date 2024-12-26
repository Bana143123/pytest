m= [1,0,1,0,1,1,0,1,1,1,0,0]
max_count=0
current_count=0
for i in m:
    if i==1:
        current_count+=1
        max_count=max(current_count,max_count)
    else:
        current_count=0

print(f"max consequent ones was : {max_count}")