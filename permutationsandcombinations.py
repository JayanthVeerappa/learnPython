def factorial(n: int) -> int:
    ans_local = 1
    for i in range(2, n + 1):
        ans_local = ans_local * i
    return ans_local





def factorials(r: int) -> int:
    ans_local = 1
    for i in range(2, r + 1):
        ans_local = ans_local * i
    return ans_local


print("Program to calculate nPr and nCr")
n = int(input("Type a number (n): "))
r = int(input("Type a number (r): "))

nminusr = int(n - r)

calculate = int(factorial(n) / (factorial(nminusr) * factorials(r)))


calculate2 = factorial(n) / factorial(nminusr)


print(f"The combination of {n} and {r} is {calculate}")
print(f"The permuatition of {n} and {r} is {calculate2}")


