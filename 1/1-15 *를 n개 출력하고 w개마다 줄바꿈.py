print('print *')
n = int(input('how many?: '))
w = int(input('line break in?: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w
if rest:
    print('*' * rest)