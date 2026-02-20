N,M = map(int,input().split())
a = [int(input()) for _ in range(N)]
a.sort()

left = 0
right = 0
ans = 10**15

while right < N:
    diff = a[right] - a[left]
    if diff < M:
        right += 1
    else:
        ans = min(ans,diff)
        left += 1
        if left > right:   # left가 right를 추월하면 right도 같이 이동
            right = left
print(ans)