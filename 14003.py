import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

lis = []
pos = [0] * n

for i in range(n):
    idx = bisect_left(lis, arr[i])

    if idx == len(lis): #맨 끝에 위치할 경우(제일 큰 값)
        lis.append(arr[i])
    else:
        lis[idx] = arr[i]

    pos[i] = idx


# LIS 복원
k = len(lis) - 1
ans = []

for i in range(n-1, -1, -1):
    if pos[i] == k:
        ans.append(arr[i])
        k -= 1

ans.reverse()

print(len(lis))
print(*ans)