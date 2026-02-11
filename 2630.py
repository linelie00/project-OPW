N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
anw = [0,0]

def div(x,y,n):
    color = paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != color:
                m = n//2
                div(x,y,m)
                div(x,y+m,m)
                div(x+m,y,m)
                div(x+m,y+m,m)
                return
    anw[color] += 1

div(0,0,N)
print(anw[0])
print(anw[1])