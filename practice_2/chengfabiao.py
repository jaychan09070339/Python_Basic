
x=1
y=1
for x in range(1,10):
    for y in range(1,x+1):
        print(x,"x",y,"=",x*y,end="   ")
        if x==y:
            print()
