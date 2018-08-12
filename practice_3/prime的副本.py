
prime=[]
while True:
    num=int(input("请输入一个数："))    
    for x in range(2,num):
        if num<2:
            break
        if num==2:
            prime.append(num)
        if num%x==0:
            print(num,"不是质数！")
            break
    else:
        print(num,"为质数！")
        prime.append(num)
        print(prime)
