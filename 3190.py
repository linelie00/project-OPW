import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())
board = [[0]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
L = int(input())
turns = deque()
for _ in range(L):
    a, b = input().split()
    turns.append([int(a), b])

time = 0 # 시간
i = 0 # 이동 정보

# L은 i+1 D는 i-1
dx = [0,-1,0,1]
dy = [1,0,-1,0]

snake = deque()
snake.append((1,1))
board[0][0] = 2

while True:
    time += 1
    x,y = snake[-1] #뱀 머리 위치
    nx = x + dx[i]
    ny = y + dy[i]

    #칸 범위 벗어날 경우
    if not (1<=nx<=N and 1<=ny<=N):
        break
    #자기 자신과 부딪힐 경우
    if board[nx-1][ny-1] == 2:
        break
    
    #사과 없으면 꼬리 지우기
    if board[nx-1][ny-1] != 1:
        ax,ay = snake.popleft()
        board[ax-1][ay-1] = 0
    
    #이동
    snake.append((nx,ny))
    board[nx-1][ny-1] = 2

    #방향전환
    if turns and time == turns[0][0]:
        _, d = turns.popleft()
        if d == 'L':
            i = (i+1)%4
        elif d == 'D':
            i = (i+3)%4
print(time)