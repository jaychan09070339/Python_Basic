
value=1
def myfac(n):
	for x in range(1,n+1):
		global value
		value*=x
	return value

print(myfac(5))

num=0
def sum_1(n):
	for x in range(1,n+1):
		global num
		num+=(x**x)
	return num

print(sum_1(3))

sum=0
def mysum(n):
	for x in range(1,n+1):
		global sum
		sum+=x
	return sum
print(mysum(100))