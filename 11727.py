n = int(input())
dp = [1] * (n)
if n >= 2:
    dp[1] = 3

for i in range(2, n):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[-1]%10007)

# 1 1
# 2 3
# 3 5
# 4 11 
# 5 21
# 6 43
# 7 85
# 8 171
