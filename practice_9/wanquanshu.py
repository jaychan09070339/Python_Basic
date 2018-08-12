
wanquanshu=[]
#num=int(input("请输入一个数：")) 
for num in range(1,9999999999):
    for x in range(1,num):
	    if num%x==0:
		    wanquanshu.append(x)
    s=sum(wanquanshu)
    if s==num:
        print(num,"是完全数！")
    wanquanshu.clear()