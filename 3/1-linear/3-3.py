from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    if i == len(seq):
        return -1
    else:
        return i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    key = int(input('검색 값을 입력하세요: '))

    index = seq_search(x, key)

    if index == -1:
        print('검색 값이 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{index}]에 있습니다.')
