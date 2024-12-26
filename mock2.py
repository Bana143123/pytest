# Write a Python program to find the indices of all occurrences of target in the uneven matrix.
# Input:
# [([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
# Output:
# [[0, 1], [0, 3], [2, 2]]

# Target value is 2
target=2
mat=[[1,2,3,2],
    [],
    [7,9,2,1,4]]
res=[]
for i,row in enumerate(mat):
    print(i,row)
    for j,value in enumerate(row):
        print(j,value)
        if value == target:
            res.append([i,j])
print(res)
            
    

