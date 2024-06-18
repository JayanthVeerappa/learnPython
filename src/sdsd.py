import random

def generate(n) -> list:
	numbers = []
	for i in range(1, n + 1):
		a = random.randint(1,100)
		numbers.append(a)
	return numbers

num = int(input("Type the number of numbers you want me to generate "))
listofnumbers = generate(num)

print(listofnumbers)
for i in range(num-1,-1,-1):
	print(listofnumbers[i])