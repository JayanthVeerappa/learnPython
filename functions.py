def my_max(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

def my_low(a, b, c):
    if (a <= b) and (a <= c):
        lowest = a

    elif (b <= a) and (b <= c):
        lowest = b
    else:
        lowest = c
    return lowest

def my_middle(a, b, c):
    if c<b<a or a<b<c:
        middle = b

    elif c<a<b or b<a<c :
        middle = a
    else:
        middle = c
    return middle