import os
path = "checking_j"
valid_json=[]
for i in os.listdir(path):
    print(i)
    if i.endswith(".json"):
        valid_json.append(i)
print(valid_json)
