N,M = map(int,input().split())
cmds = [list(map(int, input().split())) for _ in range(M)]
balls = [i+1 for i in range(N)]

for cmd in cmds:
    temp = balls[cmd[0]-1]
    balls[cmd[0]-1] = balls[cmd[1]-1]
    balls[cmd[1]-1] = temp

print(*balls)