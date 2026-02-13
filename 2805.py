N,M = map(int,input().split())
tree = list(map(int,input().split()))
left,right = 1,max(tree)

while left <= right:
    mid = (left+right)//2
    t = 0
    for x in tree:
        if x > mid:
            t += x - mid
    if t >= M: #충분히 자름 -> 높이를 더 올려본다
        left = mid + 1
    else: #너무 적게 자름
        right = mid - 1
print(right)