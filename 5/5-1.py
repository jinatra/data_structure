# 양의 정수 n의 팩토리얼 구하기

def factorial(n:int) -> int:
    # 양의 정수 n의 팩토리얼 값을 재귀적으로 구함
    if n > 0:
        return n * factorial(n-1)

    elif n == 0:
        return 1

    else:
        return


if __name__ == '__main__':
    n = int(input('팩토리얼을 구하고자 하는 n의 값을 입력: '))
    print(f'n의 팩토리얼 값은 {factorial(n)}입니다.')