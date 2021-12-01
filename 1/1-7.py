print('add integer 1 to n')

n = int(input('type n: '))

sum = 0
i = 1

while i <= n:
    sum += i      #sum = sum + i
    i += 1        # i = i + 1

print(f'final value for adding 1 to n is {sum}')
print(f'value i is {i}')