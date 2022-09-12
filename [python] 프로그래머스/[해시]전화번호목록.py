def solution(phone_book):
    answer = True
    hash = {}
    
    # 해시 테이블 만들기
    for i in phone_book:
        hash[i] = 1
    
    # phone_book 배열의 번호들을 하나씩 조회(i)함
    # 조회한 숫자(i)를 첫 글자부터 한 글자씩 추가해가면서 hash 테이블에 같은 번호가 있는지 조회함
    # 본인 숫자의 접두사가 되는 숫자가 있는지 조회함
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            # 해당 숫자의 일부분인 temp와 동일한 숫자가 hash에 있으면, 그 숫자가 접두가사 됨
            # 단, 
            if temp in hash and temp != i:  
                answer = False
                
    return answer