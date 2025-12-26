import sys
from collections import deque

input = sys.stdin.readline

def bfs(p,x,y):
    que = deque()
    que.append((x,y))
    p[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    w = 1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and p[nx][ny] == 1:
                que.append([nx, ny])
                p[nx][ny] = 0
                w += 1
    return w


n,m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
anw = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if p[i][j] == 1:
            cnt += 1
            anw = max(bfs(p,i,j), anw)
print(cnt)
print(anw)