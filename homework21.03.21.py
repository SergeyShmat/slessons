# def is_multiple(n,m):
# 	if m%n == 0:
# 		return True


# # is_multiple(2,5)

# ---------------------------------------------------
# def is_even(k):
# 	if k%2 == 0:
# 		return True

# is_even(3)
# --------------------------------------------------
def minmax(data):
	min = max = data[0]
	for i in data:
		if i >=max:
			max = i
		elif i <=min:
			min = i
		else:pass
	print((min,max))

minmax([1,3,5,6,7,0,9])

# ---------------------------------------------------
# def sum_square(n):
# 	sum = 0
# 	for i in range(1,n+1):
# 		if i%2 != 0:
# 			sum += i**2
# 	return sum


# print(sumsquare(5))


# def sum_list(a,b):
# 	lena = len(a) if len(a) < len(b) else len(b)
# 	c = list()
# 	for i in range(lena):
# 		c.append(a[i]+b[i])
# 	return c


# def sum_list2(a,b):
# 	lena = len(a) if len(a) < len(b) else len(b)
# 	return [a[i]+b[i] for i in range(lena)]

# print(sum_list2([1,2,3,4,5],[3,4,5,6,7,8,9,10]))


# try:
# 	a = [1,2,3]
# 	a[2]
# except IndexError:
# 	print("нет такого элемента")
# else:
# 	print("элемент найден")
# finally:
# 	print("завершение программы")


# a = [1,2,"one","two",3]

# for i in a:
# 	if type(i) == str:
# 		continue
# 	print(i)

# import random as ran
# print(globals())


# from price import format_price
# format_price(12.30)

# def sum_list(a,b):
# 	a.reverse()
# 	b.reverse()
# 	lena = a if len(a) < len(b) else b
# 	c = list()
# 	while lena:
# 		c.append(a.pop()+b.pop())
# 	return c

# print(sum_list([1,2,3],[1,2,3,4,5]))


# a = int(input("input any"))
# if a >1:
# 	print("ok")
# elif a >3:
# 	print("okok")
# else:
# 	print("notok")


# def string(a):
	# a = a.replace(" ","")
# 	x = '''!,.;'"?'''
# 	for i in a:
# 		if i in x:
# 			a = a.replace(i," ")
# 	print(a)

# string("hELLO,WORLD!")
	
	
# def sum_two(n):
# 	i = 0
# 	while n%2 == 0:
# 		n = n/2
# 		i = i+1
# 	return i

# print(sum_two(221.36))