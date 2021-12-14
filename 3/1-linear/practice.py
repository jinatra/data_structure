from typing import Sequence, Any

def seq_search(list: Sequence, key: Any) -> int:
    
    i = 0
    while True:
        if i == len(list):
            return -1
        if list[i] == key:
            return i
        i += 1


if __name__ == '__main__' :
    nums = int(input('원하는 원소의 갯수를 입력: '))

    list = [None] * nums

    for num in range(nums):
        list[num] = int(input(f'리스트의 {num+1}번째 원소에 원하는 숫자를 입력: '))
    
    key = int(input('찾고자 하는 숫자를 입력: '))

    results = seq_search(list, key)

    if results == -1:
        print('해당 숫자는 해당 리스트에 존재하지 않습니다.')
    else:
        print(f'해당 숫자는 리스트{list}의 {results+1}번째에 있습니다.')