K,N = map(int,input().split())
lan = [int(input()) for _ in range(K)]
left,right = 1, max(lan)

while left <= right:
    mid = (left+right)//2
    lines = 0
    for x in lan:
        lines += x//mid
    if lines >= N:
        left = mid+1
    else:
        right = mid-1
print(right)