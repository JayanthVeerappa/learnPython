n = int(input("Type a number and i will check the number of divisors it has: "))
numofdivisors= []

for i in range(1,n+1):
    if n%i==0:
        numofdivisors.append(i)
print (f"Divisors: {numofdivisors}")
print (f"The number of divisors {n} has is {len(numofdivisors)}")