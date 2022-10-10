from itertools import permutations

def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        num = str(numbers[i])
        numbers[i] = num
    
    numsort = sorted(numbers, key = lambda x:x[0], reverse=True)
    
    for i in numsort:
        answer += i
    
    # print(type(numbers[0]))
    
    # num = sorted(numbers, key = lambda x : x[0], reverse = True)
    
    
    return answer