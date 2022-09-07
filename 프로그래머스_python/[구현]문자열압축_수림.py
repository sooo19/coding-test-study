# 구현 (정답 코드)
# 문자열 압축

def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step]    # 첫번째 문자부터 step만큼의 문자열 추출
        count = 1
        
        for j in range(step, len(s), step):     # step 만큼씩 증가하면서 검사
            if s[j:j+step] == prev:     # prev에 저장된 문자열과 동일한 문자이면
                count += 1
            else:   # 다른 문자열이 나와 압축할 수 없는 형태이면 (압축 종료)
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]  # 다시 상태 초기화
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        # 남은 문자열은 뒤에 붙여주기 (aabbaab의 경우, 2개 단위로 잘랐을 때 aa/bb/aa/b로 나뉨. 마지막 b는 2개 단위로 잘리지 않으므로 끝에 그냥 붙여주기)
        # compressed += str(count) + prev   근데 왜 이건 안 되는 건지 의문 ?
        
        answer = min(answer, len(compressed))
    
    return answer