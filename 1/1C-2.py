def med3(a, b, c):
    if  a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('find middle value of three integers')
a = int(input('type integer a: '))
b = int(input('type integer b: '))
c = int(input('type integer c: '))

print(f'middle value of a, b, c is {med3(a, b, c)}')