import os
path="/home/span63/Desktop"
all=[]
for root,dirs,files in os.walk(path):
    for file in files:
        full_path=os.path.join(root,file)
        all.append(full_path)
#print(all)
for i in all:
    print(i)
#----------------------------------------------
path1="/home/span63/Desktop/mock"
for file in os.listdir(path1):
    print(file)
#----------------------------------------------

