import sys
input = sys.stdin.readline

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N):
    t, p = schedule[i]

    # 상담 안 하는 경우 (다음 날로 최대값 전달)
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담 하는 경우
    if i + t <= N:
        dp[i + t] = max(dp[i + t], dp[i] + p)

print(dp[N])
