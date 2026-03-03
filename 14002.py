import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
dp = [1]*N
prev = [-1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j

idx = dp.index(max(dp))

result = []
while idx != -1:
    result.append(A[idx])
    idx = prev[idx]

print(max(dp))
print(*result[::-1])