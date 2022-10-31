# 최솟값 만들기 문제
# : A, B 두 개의 배열이 주어질 때 A와 B 배열에서 각각 하나의 요소를 뽑아 곱한 후
# answer 변수에 누적해서 더한 값이 최소가 되는 answer 값 구하기

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        answer += A[i]*B[i]
    
    return answer