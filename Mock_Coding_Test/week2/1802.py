import sys
input = sys.stdin.readline

T = int(input())

def dir(x,n):
    global anw
    if n == 1:
        return
    #중간을 기준으로 반대
    m = n//2
    rule = True
    for i in range(x,m):
        if paper[i] == paper[n-i-1]:
            rule = False
    if not rule:
        print('NO')
        anw = False
        return
    else:
        dir(x,m)
        dir(x+m,m)

for _ in range(T):
    paper = list(map(int,input().strip()))
    anw = True
    dir(0,len(paper))
    if anw:
        print('YES')