n,k = map(int, input().split())
c = [int(input()) for _ in range(n)]
cnt = 0

for i in range(n-1,-1,-1):
    if k >= c[i]:
        cnt += k // c[i]
        k = k % c[i]
    if k == 0:
        break
print(cnt)