# 해시 자료구조 (딕셔너리 사용)
# https://codingpractices.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%8B%9C-Hash-%ED%95%B4%EC%8B%B1-Hashing-%EB%AC%B8%EC%A0%9C%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0

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
            # 단, 그 숫자가 자기자신인 경우는 제외 ("119"는 "119"의 접두사가 아님)
            if temp in hash and temp != i:  
                answer = False
                
    return answer