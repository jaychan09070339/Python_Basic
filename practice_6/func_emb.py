
def myadd(x,y):
	return x+y

def mymul(x,y):
	return x*y

def get_op(op):
	if op=="加":
		return myadd
	if op=="乘":
		return mymul

可以选择把函数嵌套进去，减少运行次数！

a=int(input("请输入第一个数："))
b=int(input("请输入第二个数："))
operator=input("请输入操作方式：")
fn=get_op(operator)
print("结果是：",fn(a,b))