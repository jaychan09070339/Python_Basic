
def dg_sum(n):
	if n==1:
		return 1
	return n+dg_sum(n-1)

print(dg_sum(100))