pos = [0] * 8

def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

print([0] * 8)