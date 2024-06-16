print ("max")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))
c = int(input("Pick a number: "))

if (a >= b) and (a >= c):
    largest = a

elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print ("The max is ", largest)
