print("prime number checker")
n = int(input("Type a number and i will check if it is a prime number: "))
numofdivisors= []

for i in range(1,n+1):
    if n%i==0:
        numofdivisors.append(i)
def primechecker():
    if len(numofdivisors)>2:
        print ("Not prime")
    else:
        print ("prime")
primechecker()
