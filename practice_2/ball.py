
#题目要求：一个球100米落下，每次落地反弹高度为原来的一半，计算
#第十次反弹高度并打印共经过多少米？
#
#方法一：循环实现
def ball_1(h,n):
	sum1=0
	for x in range(n):
		h1=h
		h=1/2*h
		sum1+=h1+h
	print("第",n,"次落地后反弹高度为",h,"米，","一共经过",sum1,"米。",sep="")

ball_1(100,10)

#方法二：递归实现
def ball2_1(n):
	if n==1:
		return 50
	return (1/2)*(ball2_1(n-1))

print(ball2_1(10))

def ball2_2(n):
	if n==1:
		return 150
	






print(ball2_2(10))
