import random
n = int(input("Type the number of numbers you want me to generate "))

numbers=[]
def generate():
	for i in range(1, n + 1):
		a = random.randint(1,100)
		numbers.append(a)

for i in numbers:
    print
