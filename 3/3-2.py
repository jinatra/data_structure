from typing import Sequence, Any

def seq_search(list: Sequence, key: Any) -> int:
    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력해주세요: '))

    list = [None] * num

    for i in range(num):
        list[i] = int(input(f'list[{i}]: '))

    answer = int(input('찾고자 하는 숫자를 입력하세요: '))

    result = seq_search(list, answer)

    if result == -1:
        print('찾고자 하는 수는 없습니다.')
    else:
        print(f'찾고자 하는 수는 리스트{list}의 {result+1} 번째에 있습니다.')
