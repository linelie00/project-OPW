T = int(input())
N = [int(input()) for _ in range(T)]
m = max(N)
dp = [0]*m
dp[0],dp[1],dp[2] = 1,1,1

for i in range(3, m):
    dp[i] = dp[i-2]+dp[i-3]

for i in N:
    print(dp[i-1])