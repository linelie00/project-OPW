N,M = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

#북-동-남-서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 0

while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1
    moved = False
    for i in range(4):
        d = (d+3)%4
        nx = r+dx[d]
        ny = c+dy[d]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            r,c = nx,ny
            moved = True
            break
    
    if not moved:
        back = (d+2)%4
        nx = r + dx[back]
        ny = c + dy[back]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
            r, c = nx, ny
        else:
            break

print(cnt)