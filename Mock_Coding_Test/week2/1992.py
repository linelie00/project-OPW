import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().strip())) for _ in range(N)]
anw = []
def quad_tree(x,y,n):
    global anw
    first = arr[x][y]
    equal = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != arr[i][j]:
                equal = False
                break
    if equal == True:
        anw.append(first)
    else:
        m = n//2
        anw.append('(')
        quad_tree(x,y,m)
        quad_tree(x,y+m,m)
        quad_tree(x+m,y,m)
        quad_tree(x+m,y+m,m)
        anw.append(')')

quad_tree(0,0,N)
print(*anw,sep='')