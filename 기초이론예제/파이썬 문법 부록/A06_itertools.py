# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))    # 모든 순열 구하기
print(result)

# 조합
from itertools import combinations
result = list(combinations(data, 2))    # 2개 뽑는 모든 조합
print(result)

# 중복 허용, 순서 바꿈 허용, 2개 뽑는 조합
from itertools import product
result = list(product(data, repeat=2))
print(result)

# 중복 허용, 순서 바꿈 허용 안함, 2개 뽑는 조합
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)