N = int(input())
triangle = [list(map(int,input().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
print(max(triangle[N-1]))

# 1(0) i
# 0 1 j
# 0 0

# 2(1) i
# 0  1  2 j
# 0 0,1 1

# 3(2)
# 0    1    2    3
# 0   0,1  1,2   2