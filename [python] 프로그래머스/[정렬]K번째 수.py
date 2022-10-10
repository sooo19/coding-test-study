def solution(array, commands):
    answer = []
    
    for arr in commands:    # arr[0]: i, arr[1]: j, arr[2]: k
        alist = array[arr[0]-1:arr[1]]
        alist.sort()
        answer.append(alist[arr[2]-1])
        
    return answer