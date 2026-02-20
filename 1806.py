N,S = map(int,input().split())
arr = list(map(int,input().split()))
left = 0
right = 0
v = arr[0]
ans = 10**15
while right < N:
    if v < S:
        right += 1
        if right < N:
            v += arr[right]
    else:
        ans = min(ans,right-left+1)
        v -= arr[left]
        left += 1
        if left>right:
            right = left
            
if ans == 10**15:
    print(0)
else:
    print(ans)