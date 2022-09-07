# 팩토리얼 예제

# 방법 1) 반복적으로 구현한 n! (iterative: 반복적인)
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 방법 2) 재귀 함수로 구현한 n!
def factorial_recursive(n):
    if n <=1:
        return 1
    return n*factorial_recursive(n-1)

print('반복문으로 구현 : ', factorial_iterative(5))
print('재귀 함수로 구현 : ', factorial_recursive(5))