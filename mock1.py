#Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# Increasing.
# Input:
# [6, 5, 4, 3, 2, 1]
# Output:
# Decreasing.
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# Not a monotonic sequence!

#d=[1, 2, 3, 4, 5, 6]
#d=[6, 5, 4, 3, 2, 1]
d=[19, 19, 5, 5, 5, 5, 5]
is_increase=True
is_decrease=True
for i in range(len(d)-1):
    if d[i]<d[i+1]:
        is_decrease=False
    elif d[i]>d[i+1]:
        is_increase=False
if is_decrease:
    print("decreasing")
elif is_increase:
    print("increasing")
else:
    print("not a monotonic sequence")

