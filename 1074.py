N,r,c = map(int,input().split())

def div(x,y,n,cnt):
    if x <= c < x+n and y <= r < y+n:
        if n == 1:
            print(cnt)
            return
        m = n//2
        div(x,y,m,cnt)
        div(x+m,y,m,cnt+(m**2))
        div(x,y+m,m,cnt+((m**2)*2))
        div(x+m,y+m,m,cnt+((m**2)*3))

div(0,0,2**N,0)