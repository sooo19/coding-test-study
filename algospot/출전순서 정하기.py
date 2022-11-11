# 문제 링크
# https://algospot.com/judge/problem/read/MATCHORDER

import sys

# c = int(sys.stdin.readline())
c = int(input())
for i in range(c):
    # n = int(sys.stdin.readline())
    # team_a = sys.stdin.readline().rstrip().split(" ")
    # team_b = sys.stdin.readline().rstrip().split(" ")

    n = int(input())
    team_a = list(map(int, input().split(" ")))
    team_b = list(map(int, input().split(" ")))


    team_a.sort()
    team_b.sort()

    answer = 0
    for a in team_a:
        for b in team_b:
            if a <= b:
                answer += 1
                team_b.remove(b)
    print(answer)


    