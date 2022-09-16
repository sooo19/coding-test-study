# 백준 4949번 : 균형 잡힌 세상

# tip)
# 괄호가 (] 또는 [)로 묶이는 것도 균형 잡히지 않은 것이기 때문에 고려해야 함

def solution(i):
    stack = []
    
    for j in list(i):
        if j == '(' or j == '[':    # 여는 괄호인 경우 stack에 추가
            stack.append(j)
        elif j == ')':      # 닫힘 소괄호이면, stack 안에 아무 것도 들어있지 않거나 [ 로 열려있는 상태일 경우 불균형이라고 판단
            if len(stack) == 0 or stack[-1] != '(':
                return 'no'
            else:
                stack.pop()
        elif j == ']':
            if len(stack) == 0 or stack[-1] != '[':     
                return 'no'
            else:
                stack.pop()

    if len(stack) == 0:
        return 'yes'
    else:
        return 'no'


input_str = []
while True:
    s = str(input())    # 입력 받은 문장
    if s == '.':
        break
    else:
        input_str.append(s)

for i in input_str:
    print(solution(i))