import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
anw = 0
def find(idx,money):
    global anw
    if idx >= N:
        anw = max(anw,money)
        return
    elif idx == N-1:
        if arr[idx][0] == 1: 
            money += arr[idx][1]
        anw = max(anw,money)
        return
    if arr[idx][0]+idx > N:
        find(idx+1,money)
        return
    else:
        find(idx+arr[idx][0],money+arr[idx][1])
        find(idx+1,money)

find(0,0)
print(anw)