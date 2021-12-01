def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b

    if c > maximum:
        maximum = c

    return maximum

print(f'max3(1, 5, 0)={max3(1, 5, 0)}')