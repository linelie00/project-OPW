import sys
from collections import deque

input = sys.stdin.readline

M,N,K = map(int,input().split())
visited = [[False]*M for _ in range(N)]
for _ in range(K):
    lx,ly,rx,ry = map(int,input().split())
    for i in range(lx,rx):
        for j in range(ly,ry):
            visited[i][j] = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    cnt = 1
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                que.append((nx,ny))
    return cnt

anw = []
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = True
            anw.append(bfs(i,j))
print(len(anw))
anw.sort()
print(*anw)