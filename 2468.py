from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(k,x,y):
    que = deque([(x,y)])
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx,ny))


ans = 1
max_v = 0
for row in graph:
    max_v = max(max_v,max(row))

for k in range(1,max_v):
    cnt = 0
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                bfs(k,i,j)
                cnt += 1
    ans = max(ans,cnt)
    
print(ans)