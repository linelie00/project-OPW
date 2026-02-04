from collections import deque

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
que = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def roll(x,y,i):
    cnt = 0
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if board[nx][ny] == '#':
            break
        x,y = nx,ny
        cnt += 1
        if board[x][y] == 'O':
            break
    return x,y,cnt


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j

visit[rx][ry][bx][by] = True
que.append((rx,ry,bx,by,0))

while que:
    rx,ry,bx,by,depth = que.popleft()
    if depth >= 10:
        continue
    for i in range(4):
        rnx,rny,rcnt = roll(rx,ry,i)
        bnx,bny,bcnt = roll(bx,by,i)

        if board[bnx][bny] == 'O':
            continue
        if board[rnx][rny] == 'O':
            print(1)
            exit()
        
        if rnx == bnx and rny == bny:
            if rcnt > bcnt:
                rnx -= dx[i]
                rny -= dy[i]
            else:
                bnx -= dx[i]
                bny -= dy[i]

        if not visit[rnx][rny][bnx][bny]:
            visit[rnx][rny][bnx][bny] = True
            que.append((rnx,rny,bnx,bny,depth+1))
print(0)