import sys
from collections import deque

input = sys.stdin.readline

M,N,H = map(int, input().split())
board = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
time = 0

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

que = deque()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 1:
                que.append((h,i,j))

while que:
    h,x,y = que.popleft()
    for i in range(6):
        nh = h + dh[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nh<H and 0<=nx<N and 0<=ny<M and board[nh][nx][ny] == 0:
            board[nh][nx][ny] = board[h][x][y] + 1
            que.append((nh,nx,ny))

for h in range(H):
    for i in range(N):
        for j in range(M):
            if board[h][i][j] == 0:
                print(-1)
                exit()
            time = max(time,board[h][i][j])
print(time-1)