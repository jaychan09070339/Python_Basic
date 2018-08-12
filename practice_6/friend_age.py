
text=int(input("请输入朋友数："))
ori_age=int(input("第一个朋友岁数："))

def age(n):
	if n==1:
		return ori_age
	else:
		return age(n-1)+2


print("第",text,"个朋友",age(text),"岁")