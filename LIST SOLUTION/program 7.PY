
def channame(li):
    name=[]
    x=".c"
    for i in li:
        if x in i: 
            y=i.replace(".c",".py")
            name.append(y)
        else:
            name.append(i)    

    print(name)    

f= ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
channame(fi)