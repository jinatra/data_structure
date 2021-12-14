from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    # 시퀀스 a에서 key와 일치하는 원소를 이진 검색
    left = 0                 # 검색 범위 맨 앞 원소의 인덱스
    right = len(a) - 1       # 검색 범위 맨 끝 원소의 인덱스

    while True:
        center = (left + right) // 2    # 중앙 원소의 인덱스
        if a[center] == key:
            return center               # 검색 성공

        elif a[center] < key:
            left = center + 1           # 검색 범위를 뒤쪽 절반으로 좁힘

        else:
            right = center - 1          # 검색 범위를 앞쪽 절반으로 좁힘

        if left > right:
            break

    return -1                            # 검색 실패


a = [1,2,3,4,5,6,7,8,9,10,44,44]
key = 44

print(bin_search(a, key))