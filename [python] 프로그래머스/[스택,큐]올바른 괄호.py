def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    
    # 괄호 쌍을 모두 뺐는데도 stack에 (가 남아있다면, False를 리턴 
    # 닫는 괄호가 부족한 상황임
    if len(stack) > 0:      
        return False
    
    return True