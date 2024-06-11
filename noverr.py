print ("is it divisible?")
while True:
    n = int(input("Pick a number (n): "))
    r = int(input("Pick a number (r): "))
    if n%r == 0 :
        print ("This is divisble")
        again = input ("do you want to try again? (y/n)")
        if again == "y":
            continue
        else:
            break
    else:
        print("This is not divisble")
        again = input ("do you want to try again? (y/n)")
        if again == "y":
            continue
        else:
            break
