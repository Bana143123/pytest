n=[1,2,3,4,5,6]
target = int(input("Enter the targeted number here:  "))
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i] + n[j] == target:
            print(f"Target was match with these pairs {n[i],n[j]}")