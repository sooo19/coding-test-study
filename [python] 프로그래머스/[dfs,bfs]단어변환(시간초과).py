# 시간 초과 코드

def solution(begin, target, words):    
    if target not in words:     # target 단어가 words 배열에 없으면 0을 리턴
        return 0
    
    answer = 0
    while(1):
        arr = [0 for _ in range(len(words))]    # words 배열과 같은 길이의 배열을 생성해서 현재 begin과 배열 안 각 단어들의 글자 수 차이를 기록함
        for s in range(len(words)):
            val = 0
            for i in range(len(words[s])):
                if begin[i] != words[s][i]:
                    val += 1
            arr[s] = val

        for i in range(len(arr)):   # arr 배열에 기록한 숫자를 통해 한 자리만 다른 단어를 begin 값으로 교체
            if arr[i] == 1:
                begin = words[i]
        answer += 1     # 교체할 때마다 교체 횟수를 1씩 증가시킴
        
        if target == begin:
            return answer