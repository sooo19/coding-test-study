# 모음 사전 구현 후, word 단어가 해당 사전에서 몇 번째 index를 가지는지 리턴하는 방식

from itertools import product
def solution(word):
    answer = 0
    
    total_dict = []
    for i in range(1, 6):
        dictionary = list(map("".join, product(['A','E','I','O','U'], repeat = i)))
        total_dict.extend(dictionary)
    
    total_dict.sort()
    for i in range(len(total_dict)):
        if total_dict[i] == word:
            answer = i+1
    return answer