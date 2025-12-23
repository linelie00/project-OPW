import sys

input = sys.stdin.readline

t = int(input())
s=[int(input()) for _ in range(t)]
m = max(s)
dp = [[0] * (m+1) for _ in range(2)]

dp[0][0] = 1
dp[1][0] = 0
if m >= 1:
    dp[0][1] = 0
    dp[1][1] = 1
if m >= 2:
    for i in range(2,m+1):
        dp[0][i] = dp[0][i-1] + dp[0][i-2]
        dp[1][i] = dp[1][i-1] + dp[1][i-2]

for i in s:
    print(dp[0][i],dp[1][i])