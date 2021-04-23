import random
b = []
def random_item(n):
	a = len(n)
	for i in n:
		i = random.randomrange(n[0],n[a-1])
		b.append(i)

		return b

print(random_item([1,2,3,4,5,6,7]))
