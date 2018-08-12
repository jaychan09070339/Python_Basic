
num=int(input("请输入一个数字："))
x=1
for x in range(1,num+1):
    print(("*"*(2*x-1)).center(2*num-1))
y=1
for y in range(1,num+1):
    print("*".center(x*2-1))
