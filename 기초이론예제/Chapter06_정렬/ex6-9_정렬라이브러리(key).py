# 정렬 라이브러리에서 key를 활용한 소스코드

array = [('바나나, 2'), ('사과', '5'), ('당근, 3')]

def setting(data):
    return data[1]      # data[1] 값을 기준으로 정렬

result = sorted(array, key = setting)
print(result)