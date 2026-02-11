from collections import deque

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
b_visited = [[False]*N for _ in range(N)]
anw = [0,0]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    que = deque()
    que.append((x,y))
    visited[x][y] = True
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == color:
                    visited[nx][ny] = True
                    que.append((nx,ny))
def b_bfs(x,y,color):
    b_que = deque()
    b_que.append((x,y))
    b_visited[x][y] = True
    while b_que:
         x,y = b_que.popleft()
         for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
              if 0 <= nx < N and 0 <= ny < N and not b_visited[nx][ny]:
                   if graph[nx][ny] == color or (color in 'RG' and graph[nx][ny] in 'RG'):
                        b_visited[nx][ny] = True
                        b_que.append((nx,ny))

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            anw[0] += 1
            bfs(i,j,graph[i][j])
        if not b_visited[i][j]:
            anw[1] += 1
            b_bfs(i,j,graph[i][j])
print(anw[0],anw[1])