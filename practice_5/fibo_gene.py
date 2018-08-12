
count=3
def fibonacci(n):
	x=1
	y=1
	yield 1
	yield 1
	global count
	while count<=n:
		sum=x+y
		yield sum
		x=y
		y=sum
		count+=1

for x in fibonacci(10):
	print(x)

def myodd(n):
	x=1
	while x<=n:
		yield x
		x+=2

for y in myodd(10):
	print(y)
