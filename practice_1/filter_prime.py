
def prime_1(n):
	if n==0:
		return False
	if n==1:
		return False
	if n==2:
		return 2
	else:
		for x in range(2,n):
			if n%x==0:
				return False
			else:
				pass
		else:
			return True


L=[x for x in filter(prime_1,range(101))]
print(L)


