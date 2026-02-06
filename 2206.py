from collections import deque

n,m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
que = deque()
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

que.append((0,0,0,1))
visited[0][0][0] = True

while que:
    x,y,w,cnt = que.popleft()

    if x == n-1 and y == m-1:
        print(cnt)
        exit()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < m):
            continue

        if graph[nx][ny] == 0 and not visited[nx][ny][w]:
            visited[nx][ny][w] = True
            que.append((nx, ny, w, cnt + 1))

        elif graph[nx][ny] == 1 and w == 0 and not visited[nx][ny][1]:
            visited[nx][ny][1] = True
            que.append((nx, ny, 1, cnt + 1))
print(-1)