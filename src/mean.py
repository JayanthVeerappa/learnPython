def calculate(numbers):
    sum= 0
    for number in numbers:
        sum= sum+number

    mean =sum/len(numbers)
    return (mean)
def calculator():
    print ("Math calculator")
    numbers = []
    n=int(input("how many numbers do you want me to calculate with?:"))
    for index in range(n):
        what= int(input("what is the number you want me to calculate with?:"))
        print(what)
        numbers.append(what)
        print (numbers)
    mean=calculate(numbers)
    print("The mean is",mean)
    add = int(input("what other numbers do you want me to add?:"))
    numbers.append(add)
    new= calculate(numbers)
    print("The new mean is",new)
calculator()
again = input("Do you wanT do this again?: ")
if again == "yes":
    calculator()
elif again == "no":
    print ("ok goodbye")




