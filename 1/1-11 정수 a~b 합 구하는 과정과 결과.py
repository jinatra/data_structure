print('add integers a through b')
a = int(input('type a: '))
b = int(input('type b: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end = '')
    sum += i

print(f'{b} = ', end = '')
sum += b

print(sum)