import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    a = int(input())
    if a == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq,a)