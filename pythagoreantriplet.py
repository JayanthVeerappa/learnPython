from src.functions import my_max, my_low, my_middle

print ("pythagorean triplet")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))
c = int(input("Pick a number: "))
largest = my_max(a, b, c)

low = my_low(a,b,c)
middle = my_middle(a,b,c)
print(f"Low is {low}")
print(f"middle is {middle}")
if my_low(a,b,c)**2 +my_middle(a,b,c)**2 == largest**2:
   print ("It is a pythagorean triplet")
else:
    print ("it is not a pythagorean triplet ")
