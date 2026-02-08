n = int(input())
road = list(map(int,input().split()))
city = list(map(int,input().split()))

dp = [0]*n
m = city[0]

for i in range(1,n):
    dp[i] = dp[i-1] + m*road[i-1]
    m = min(m,city[i])

print(dp[-1])