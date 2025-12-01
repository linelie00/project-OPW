import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]
for i in range(n):
    dp.append(dp[i]+arr[i])

for i in range(m):
    i,j = map(int, input().split())
    print(dp[j]-dp[i-1])