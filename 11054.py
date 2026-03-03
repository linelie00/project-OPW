N = int(input())
A = list(map(int,input().split()))
dp = [1]*N
re_dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
        if A[N-j-1] < A[N-i-1] and re_dp[N-i-1] < re_dp[N-j-1] + 1:
            re_dp[N-i-1] = re_dp[N-j-1] + 1
print(max(dp[i]+re_dp[i] for i in range(N))-1)