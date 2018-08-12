
x=1
y=1
count=0
while True:
    if count<2:
        print(1,end=" ")
        count+=1
    else:
        num=x+y
        print(num,end=" ")
        count+=1
        x=y
        y=num
        if count>=18:
            break
    
    
