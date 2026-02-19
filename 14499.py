import sys
input = sys.stdin.readline

N,M,x,y,K = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(N)]
cmd = list(map(int,input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0,0,0,0,0,0] #위앞밑뒤왼오

def turn(dir):
    a,b,c,d,e,f = dice  # 위,앞,밑,뒤,왼,오

    if dir == 1:      # 동
        dice[0], dice[4], dice[2], dice[5] = e, c, f, a
    elif dir == 2:    # 서
        dice[0], dice[5], dice[2], dice[4] = f, c, e, a
    elif dir == 4:    # 남
        dice[0], dice[3], dice[2], dice[1] = d, c, b, a
    elif dir == 3:    # 북
        dice[0], dice[1], dice[2], dice[3] = b, c, d, a

for i in cmd:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if 0<=nx<N and 0<=ny<M:
        turn(i)
        if m[nx][ny] == 0:
            m[nx][ny] = dice[2]
        else:
            dice[2] = m[nx][ny]
            m[nx][ny] = 0
        print(dice[0])
        x,y = nx,ny