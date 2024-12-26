def check():
    with open("inp.txt","r") as file:
        lines=file.readlines()
        x=(len(lines))
        print(x)
        lines.append(x)
        print(lines)
    with open("inp.txt","a") as f:
        f.write(str(x))
        
        

res=check()
