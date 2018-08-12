
def sum3(a,b,c):
	return a+b+c

def pow3(x):
	return x**3

print(sum3(pow3(1),pow3(2),pow3(3)))
print(pow3(1+2+3))

def sum4(a=0,b=0,c=0,d=0):
	return a+b+c+d

def minmax(*args):
	if len(args)<2:
		print("参数太少！")
	min_value=min(args)
	max_value=max(args)
	return (min_value,max_value)


print(sum4(1,2))
print(sum4(1.1,2.2,3.3))
print(sum4(100,200,300,400))
