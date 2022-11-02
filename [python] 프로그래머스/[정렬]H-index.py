def solution(citations):    
    citations.sort()
    c_length = len(citations)
    
    for i in range(c_length):
        if citations[i] >= c_length - i:      # c_length - (i+1) + 1
            return c_length-i
        
    return 0

# 답이 없으면 0을 리턴해야 하는 건가?
