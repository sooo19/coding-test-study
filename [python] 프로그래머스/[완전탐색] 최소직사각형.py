def solution(sizes):
    answer = 0
    
    garo = []	# 가로 값들을 모두 저장
    saero = []	# 세로 값들을 모두 저장
    for i in range(len(sizes)):
        garo.append(sizes[i][0])
        saero.append(sizes[i][1])
    
    max_length = max(max(garo), max(saero))		# 가로, 세로 통틀어 가장 긴 값을 찾아 max_length에 저장
    
    if max_length in garo:		# 최댓값이 가로에 있다면
        for i in range(len(garo)):		# 최댓값을 제외한 나머지 값들 중, 가로 < 세로인 경우를 찾아 서로 값을 바꿔준다.
            if garo[i] < saero[i]:
                garo[i], saero[i] = saero[i], garo[i]
        answer = max_length * max(saero)	# 최댓값(가로)*세로의 최댓값이 최종 정답
    elif max_length in saero:	# 최댓값이 세로에 있다면
        for i in range(len(garo)):		# 최댓값을 제외한 나머지 값들 중, 가로 > 세로인 경우를 찾아 서로 값을 바꿔준다.
            if garo[i] > saero[i]:
                garo[i], saero[i] = saero[i], garo[i]
        answer = max_length * max(garo)		# 최댓값(세로)*가로의 최댓값이 최종 정답
    
    return answer