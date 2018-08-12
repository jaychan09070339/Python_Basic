
n=int(input("请输入斐波那契输出个数："))
x=1
y=1
count=1
Fibonacci=[]
if n==0:
    print("数据有误！请重新输入！")
else:
    while True:
        if 0<n<3:
            for m in range(1,n+1):
                Fibonacci.append(1)
            break
        else:
            Fibonacci.insert(0,1)
            Fibonacci.insert(1,1)
            for count in range(1,n-1):
                num=x+y
                Fibonacci.append(num)
                x=y
                y=num
                count+=1
            break
    print(Fibonacci)
