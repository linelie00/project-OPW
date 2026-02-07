import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(k+1) #각 무게를 가질 때의 최댓값

for w,v in bag:
    for weight in range(k, w - 1, -1): #k부터 w까지 -1
        dp[weight] = max(dp[weight], dp[weight - w] + v) 
print(dp[k])