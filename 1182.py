import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(i,n):
        print(i,j)
        if sum(arr[i:j+1]) == s:
            cnt += 1
print(cnt)