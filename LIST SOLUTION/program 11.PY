def madict(lis):
    di={}
    y=int(input("Enter minimum word length:"))
    for i in lis:
        if len(i)>=y:
            di[i]=len(i)

    print(di)

def put1():
    str=input("Enter sentence:")
    m=str.split(" ")
    madict(m)

put1()    