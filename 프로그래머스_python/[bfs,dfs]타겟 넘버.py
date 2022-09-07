# 프로그래머스 BFS/DFS 문제
# BFS (그동안 풀었던 BFS와는 다른 느낌)

def solution(numbers, target):
    answer = 0
    leaves = [0]

    # numbers 속 요소들은 num
    # leaves 속 요소들은 parent

    for num in numbers:
        tmp = []
        for parent in leaves:
            print('parent: ', parent, 'number: ', num)
            print('tmp: ', tmp)
            tmp.append(parent + num)
            tmp.append(parent - num)
            leaves = tmp
            print('leaves: ', leaves)
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
    return answer

print(solution([4, 1, 2, 1], 4))