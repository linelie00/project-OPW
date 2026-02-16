import sys
input = sys.stdin.readline

T,W = map(int,input().split())
num = [int(input()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T)]

if num[0] == 1:
    dp[0][0] = 1
    dp[0][1] = 0
else:
    dp[0][0] = 0
    dp[0][1] = 1

for t in range(1,T):
    for w in range(W+1):
        if w > t:
            continue
        #움직이지 않는 경우
        stay = dp[t-1][w]
        #움직이는 경우
        move = 0
        if w > 0:
            move = dp[t-1][w-1]

        dp[t][w] = max(stay,move)

        if (w % 2 == 0 and num[t] == 1) or (w % 2 == 1 and num[t] == 2):
            dp[t][w] += 1
print(max(dp[T-1]))