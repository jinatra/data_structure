# 버블 정렬 알고리즘 구현 (정순)


from typing import MutableSequence

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

a = [6, 2, 9, 1, 5, 3]

print(bubble_sort(a))