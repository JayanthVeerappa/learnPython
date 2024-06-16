import random
n = int(input("Type the number of numbers you want me to generate "))

numbers=[]
def generate():
	for i in range(1, n + 1):
		a = random.randint(1,100)
		numbers.append(a)
		print (a)

def sum():
	total = 0
	for i in range(0, len(numbers)):
		total = total + numbers[i]
	print (f"The sum of {numbers} is {total}")

def minimum():
	min = numbers[n - 1]
	for i in numbers:
		if i < min:
			i = min
	print(f"The min of {numbers} is {min}")

def maximum():
	max = numbers[0]
	for i in numbers:
		if i > max:
			i = max
	print(f"The max of {numbers} is {max}")

def mean():
	total = 0
	for i in range(0, len(numbers)):
		total = total + numbers[i]
	means = total/len(numbers)
	print (f"The mean {numbers} is {means}")

def mode():
	counter =0
	for i in numbers:
		counter = counter+1
	if counter > 1:
		print (f"The mode {numbers} is {mode}")


generate()
sum()
mean()
maximum()
minimum()
mode()



