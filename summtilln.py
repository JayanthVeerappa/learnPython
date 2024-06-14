def sum(n: int) -> int:
	ans_local = 1
	for i in range(2, n + 1):
		ans_local = ans_local + i
	return ans_local


print("Program to print the sum of all the numbers till n")
n = int(input("Type a number (n): "))
ans = sum(n)
print(f"The factorial of {n} is {ans}")
