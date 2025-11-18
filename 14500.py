n, m = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
ans = 0

# 가로 4
for i in range(n):
    for j in range(m-3):
        ans = max(ans, sum(arr[i][j+k] for k in range(4)))
# 세로 4
for i in range(n-3):
    for j in range(m):
        ans = max(ans, sum(arr[i+k][j] for k in range(4)))
#가로 2 세로 2
for i in range(n-1):
    for j in range(m-1):
        ans = max(ans, arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1])
        if j < m-2:
            ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j+2])
            ans = max(ans, arr[i][j+1] + arr[i][j+2] + arr[i+1][j] + arr[i+1][j+1])
        if i < n-2:
            ans = max(ans, arr[i][j] + arr[i+1][j] + arr[i+1][j+1] + arr[i+2][j+1])
            ans = max(ans, arr[i+1][j] + arr[i+2][j] + arr[i][j+1] + arr[i+1][j+1])
            
#가로 3 세로 1
for i in range(n):
    for j in range(m-2):
        temp = sum(arr[i][j+k] for k in range(3))
        if i != n-1:
            ans = max(ans, temp + max(arr[i+1][j+k] for k in range(3)))
        if i != 0:
            ans = max(ans, temp + max(arr[i-1][j+k] for k in range(3)))

#가로 1 세로 3
for i in range(n-2):
    for j in range(m):
        temp = sum(arr[i+k][j] for k in range(3))
        if j != m-1:
            ans = max(ans, temp + max(arr[i+k][j+1] for k in range(3)))
        if j != 0:
            ans = max(ans, temp + max(arr[i+k][j-1] for k in range(3)))

print(ans)