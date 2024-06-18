import random
n = int(input("Type the number of numbers you want me to generate "))
m = int(input("Type the number of numbers you want me to generate "))
list1=[]
list2=[]
def generate():
    for i in range(1, n + 1):
        a = random.randint(1,10)
        list1.append(a)
    print (list1)


    for i in range(1, m + 1):
        a = random.randint(1, 10)
        list2.append(a)
    print(list1)

generate()