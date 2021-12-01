# 버블 정렬 알고리즘 구현 (역순 + exchng)

from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        print(exchng)
        if exchng == 0:
            break
    return a

a = [2, 3, 4, 5, 1]

print(bubble_sort(a))
