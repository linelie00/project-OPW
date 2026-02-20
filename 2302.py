N = int(input())
M = int(input())
start = 0
dist = []
for _ in range(M):
    a = int(input())
    dist.append(a-start-1)
    start = a
dist.append(N-start)

m = max(dist)
dp = [0]*(m+1)
dp[0] = 1
if m >= 1:
    dp[1] = 1
if m > 1:
    dp[2] = 2
for i in range(3,m+1):
    dp[i] = dp[i-1]+dp[i-2]

anw = 1
for x in dist:
    anw *= dp[x]

print(anw)

#1 1
#2 2
#3 3
#4 5
#5 8

# 1 2 3
# 2 1 3
# 1 3 2

# 1 2 3 4
# 2 1 3 4
# 2 1 4 3
# 1 3 2 4
# 1 2 4 3

# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 2 1 3 5 4
# 1 3 2 4 5
# 1 3 2 5 4
# 1 2 4 3 5
# 1 2 3 5 4