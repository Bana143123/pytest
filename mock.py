def check(path):
    with open(path,"r") as file:
        lines=file.read()
        print(lines)
        d=lines.split()
        #print(d)
        re=[]
        for i in d:
            if d.count(i)>1 and i not in re:
                re.append(i)
        return " ".join(re)

path = "inp.txt"
res = check(path)
print(res)