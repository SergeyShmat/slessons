
mem = {}
def factorial_mem(n):
	if n <2:
		return 1
	if n not in mem:
		mem[n] = n*factorial_mem(n-1)
		return mem[n]
		

a = factorial_mem(10)
print(a)