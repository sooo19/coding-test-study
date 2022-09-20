# input() 함수보다 빠르게 입력 받는 방법
# sys 라이브러리 사용

import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)