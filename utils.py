def factorial(n):
	res = 1
	for i in range(1, n+1):
		res*=i
	return res

def is_pow_2(n):
	while !(n%2) and n!=1:
		n//=2
	return n==1


