def changenum(lis):
    n=[]
    b1=int(input("Enter value to replace:"))
    c1=int(input("Enter value change with:"))
    for i in lis:
        if b1==i:
            n.append(c1)
        else:
            n.append(i)    
    print(n)

def crealist():
    li=[]
    b=int(input("numbers to enter in list:"))
    for i in range(b):
        c=int(input("Enter a number:"))
        a.append(c)
    changenum(li)

crealist()