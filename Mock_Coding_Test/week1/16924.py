n,m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
mark = [[False]*m for _ in range(n)]
cross = []
cnt = 0
min_v = min(n,m)

def find_cross(x,y):
    s = 0
    mark[x][y] = True
    for i in range(1,min_v+1):
        if i <= x < n-i and i <= y < m-i:
            if board[x+i][y] != '.' and board[x-i][y] != '.' and board[x][y+i] != '.' and board[x][y-i] != '.':
                s += 1
                mark[x+i][y] = True
                mark[x-i][y] = True
                mark[x][y+i] = True
                mark[x][y-i] = True
            else:
                break
        else:
            break
    return s

for i in range(n):
    for j in range(m):
        if board[i][j] == '.':
            continue
        s = find_cross(i,j)
        if s:
            cross.append((i+1,j+1,s))

for i in range(n):
    for j in range(m):
        if board[i][j] == '*' and not mark[i][j]:
            print(-1)
            exit()

print(len(cross))
for row in cross:
    print(*row)