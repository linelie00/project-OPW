import math

n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        if i != 1:
            cnt += 1

print(cnt)