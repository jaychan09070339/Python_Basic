
prime_list=list()
def isprime(x):
	if x<2:
	    return False
	elif x==2:
		return True
	else:
		for i in range(2,x):
			if x%i==0:
				return False
				break
		else:
			return True


def prime_m2n(m,n):
	prime_list.clear()
	for x in range(m,n+1):
		if isprime(x)==True:
			prime_list.append(x)
	return prime_list


def primes(n):
	prime_list.clear()
	return prime_m2n(2,n)




S=primes(100)
print(S)
L=prime_m2n(2,7)
print(L)
Q=primes(1000)
print(Q,end=" ")
print()
R=prime_m2n(1,200)
print(R,end=" ")
# isprime(1)
# isprime(2)
# isprime(3)
# isprime(4)
# isprime(17)
# isprime(23)
# isprime(36)
