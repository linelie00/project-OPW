n = int(input())

dp = [0] * (n+1)
use_num = [[] for _ in range(n+1)]
use_num[1] = [1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    best_prev = i - 1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        best_prev = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        best_prev = i//3

    use_num[i] = use_num[best_prev] + [i]

print(dp[n])
print(*reversed(use_num[n]))
