n,k = map(int, input().split())
arr = [[0]*6 for _ in range(2)]

for _ in range(n):
    s,y = map(int, input().split())
    arr[s][y-1] += 1

print(sum((x + k - 1) // k for row in arr for x in row))