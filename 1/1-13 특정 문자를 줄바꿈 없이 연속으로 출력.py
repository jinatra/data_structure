print('print + and - by turns')
n = int(input('how many times: '))

for _ in range(n // 2):
    print('+-', end = '')

if n % 2:
    print('+', end='')

print()