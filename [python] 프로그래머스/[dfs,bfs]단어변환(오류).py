def solution(begin, target, words):    
    if target not in words:     # target 단어가 words 배열에 없으면 0을 리턴
        return 0
    
    answer = 0
    while target != begin:      # target 값에 도달하지 못한 경우 while문 반복 
        for s in words:        
            d = 0
            for i in range(len(s)):
                if begin[i] != s[i]:      # begin과 s 단어의 각 자리가 같은지 비교
                    d += 1      # 다르면 변수에 1을 더해 기록
            
            print("d: ", d)

            change = 0
            if d == 1:      # 한 자리만 다른 단어이면
                begin = s       # 단어를 바꿔줌
                print("s: ", s)
                change += 1     # 단어를 바꾸는 경우를 기록
            else:
                continue
            
            print("change: ", change)

            if change == 1:
                answer += 1
                print("answer: ", answer)

        return answer