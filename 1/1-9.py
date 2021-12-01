print('add integers a through b')
a = int(input('type a: '))
b = int(input('type b: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    sum += i

print(f'result for adding {a} through {b} is: {sum}')