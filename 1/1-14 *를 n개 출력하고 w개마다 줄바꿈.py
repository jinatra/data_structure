print('print *')
n = int(input('how many?: '))
w = int(input('line break in?: '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()

if n % w:
    print()