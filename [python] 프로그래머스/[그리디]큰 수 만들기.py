# 다시 풀어보기
def solution(number, k):
    answer = ''
    
    number = list(number)       # number 배열을 리스트화
    stack = [number.pop(0)]    # number 배열의 첫 번째 요소를 result에 삽입 (괄호 안에 입력한 번호를 인덱스로 가지는 요소가 pop됨)
    
    for n in number:
        if stack[-1] < n:      # result의 가장 마지막 값이 n보다 작으면
            while stack and stack[-1] < n and k > 0:
                stack.pop()     # 괄호 안에 아무런 숫자 없이 배열을 pop하면 뒤에서부터 값이 삭제됨
                k -= 1
            stack.append(n)        # result 배열의 뒤에서부터 n보다 작은 숫자들을 모두 제거한 후, n 값을 삽입
        elif k == 0 or stack[-1] >= n:
            stack.append(n)        # 바로 n 값을 삽입
    
    if k > 0:   # 아직 k개의 수가 제거되지 않은 경우
        stack = stack[0:-k]       # 뒤에서부터 제거
    answer = ''.join(stack)
            
    
    return answer