from collections import deque

n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visit = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)] # 4차원 list로 방문한 좌표(rx,ry,bx,by) 저장
que = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#roll 함수
def roll(x,y,i):
    cnt = 0
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        # #을 만났을 때
        if board[nx][ny] == '#':
            break
        x = nx
        y = ny
        cnt +=1
        # O에 도달했을 때
        if board[nx][ny] == 'O':
            break
    return x,y,cnt


for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx,ry = i,j
        elif board[i][j] == 'B':
            bx,by = i,j

que.append((rx,ry,bx,by,0)) #R의 x,y좌표/B의 x,y좌표/깊이

while que:
    rx,ry,bx,by,depth = que.popleft()

    if depth >= 10:
        continue

    for i in range(4):
        #r을 roll 했을 때의 결과 (x,y좌표 및 카운트)
        rnx,rny,rcnt = roll(rx,ry,i)
        #b를 roll 했을 때의 결과 (x,y좌표 및 카운트)
        bnx,bny,bcnt = roll(bx,by,i)

        #b가 O에 들어갔을 때 (오답 처리)
        if board[bnx][bny] == 'O':
            continue
        
        #r이 O에 들어갔을 때 (정답 처리)
        if board[rnx][rny] == 'O':
            print(depth+1)
            exit()

        #r과 b가 겹쳤을 때 (이동 거리를 보고 옮기기)
        if rnx == bnx and rny == bny:
            if rcnt > bcnt:
                rnx -= dx[i]
                rny -= dy[i]
            else:
                bnx -= dx[i]
                bny -= dy[i]

        #방문하지 않은 좌표일 때 (rnx,rny,bnx,bny,depth+1 append하기)
        if visit[rnx][rny][bnx][bny] == False:
            visit[rnx][rny][bnx][bny] = True
            que.append((rnx,rny,bnx,bny,depth+1))

#정답이 없는 경우 -1 출력
print(-1)