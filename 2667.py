import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
anw = 0
num_anw = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    cnt = 1
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                que.append((nx,ny))
    return cnt

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            anw += 1
            cnt = bfs(i,j)
            num_anw.append(cnt)

print(anw)
num_anw.sort()
for i in range(anw):
    print(num_anw[i])