# 피보나치 함수 (재귀로 구현)

# 아래 코드의 문제점 : f(n) 함수에 n이 커질수록 수행 시간이 기하급수적으로 늘어난다

def fibo(x):
    if x == 1 or x == 2:        # f(1)과 f(2)는 1이다
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

print(fibo(4))