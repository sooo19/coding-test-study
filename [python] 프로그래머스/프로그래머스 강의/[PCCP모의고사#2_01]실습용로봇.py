# R L G(전진) B(후진)
def solution(command):    
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 12시, 3시, 6시, 9시 방향을 바라보며 1칸 전진
    x = 0   # x좌표
    y = 0   # y좌표
    d = 0   # 방향 (dxy 배열의 d번째 배열을 선택해 좌표이동함)
    
    for c in command:
        if c == 'R':
            d = (d+1)%4
        elif c == 'L':
            d = (d-1)%4
        elif c == 'G':
            x = x + dxy[d][0]
            y = y + dxy[d][1]
        elif c == 'B':
            x = x - dxy[d][0]
            y = y - dxy[d][1]
    
    return [x, y]