n = int(input())

stars = [[' ']*(n*2) for _ in range(n)]

def find(x,y,n):
    if n == 3:
        stars[x][y] = '*'
        stars[x+1][y-1] = '*'
        stars[x+1][y+1] = '*'
        stars[x+2][y-2:y+3] = ['*']*5
        return
    m = n//2
    find(x,y,m)
    find(x+m,y-m,m)
    find(x+m,y+m,m)

find(0,n-1,n)
for row in stars:
    print(''.join(row))