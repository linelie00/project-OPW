import math

n = int(input())
INF = 10**15
dp = [[INF,INF] for _ in range(n+1)]
dp[0] = [0,0] #0일, 물을 0만큼 줌

for i in range(1,n+1):
    dp[i] = min(dp[i],[dp[i-1][0]+1,dp[i-1][1]+1])
    if i%3 == 0:
        dp[i] = min(dp[i],[dp[i//3][0]+1,dp[i//3][1]+3])
    root = int(math.isqrt(i))
    if root * root == i and root < i:
        dp[i] = min(dp[i], [dp[root][0]+1, dp[root][1]+5])

print(*dp[-1])