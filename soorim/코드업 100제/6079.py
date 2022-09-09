# [기초-종합] 언제까지 더해야 할까?
a = int(input())
sum, add = 0, 0
while sum < a:
    add += 1
    sum += add

print(add)
