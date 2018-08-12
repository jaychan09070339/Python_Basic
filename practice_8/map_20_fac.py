
fac=1
sum1=0
def fac_1(n):
	global fac
	fac*=n
	return fac

for x in map(fac_1,range(1,6)):
	sum1+=x
print(sum1)

