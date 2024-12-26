path="/home/span63/Desktop/mock"
import os
for i in os.listdir(path):
    print(i)


path2="/home/span63/Desktop"

for root,dirs,files in os.walk(path2):
    for file in files:
        full_path=os.path.join(root,file)
        print(full_path)