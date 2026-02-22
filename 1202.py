import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().split())
jewel = [list(map(int,input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
jewel.sort()
bag.sort()
heap = []
idx = 0
ans = 0
for x in bag:
    while idx<N and jewel[idx][0] <= x:
        heapq.heappush(heap,-jewel[idx][1])
        idx += 1
    ans += -heapq.heappop(heap)
    
print(ans)