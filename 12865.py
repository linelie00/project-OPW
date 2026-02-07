import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(k+1) #각 무게 넘지 않게 담았을 때 얻을 수 있는 최댓가치

for w,v in bag:
    for weight in range(k, w - 1, -1): #k부터 w까지 -1
        dp[weight] = max(dp[weight], dp[weight - w] + v) #현재 무게를 만들 때 가치가 큰 것 선택
print(dp[k])