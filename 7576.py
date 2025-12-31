import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            que.append((i, j))

while que:
    x,y = que.popleft()
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            que.append((nx,ny))

ans = 0
for row in box:
    if 0 in row:
        print(-1)
        exit()
    ans = max(ans, max(row))

print(ans - 1)