
number=list()
num=int(input("请输入一个数字："))

def f_2(n):
	def f_1(n):
		for x in range(2,n):
			if n%x==0:
				number.append(x)
				return x
	n=n//f_1(n)
	return number


print(f_2(num))
