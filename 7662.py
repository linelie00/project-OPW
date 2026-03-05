import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())

    min_hq = []
    max_hq = []
    nums = {}
    
    for _ in range(k):
        cmd = list(input().split())

        if cmd[0] == 'I':
            v = int(cmd[1])
            heapq.heappush(min_hq,v)
            heapq.heappush(max_hq,-v)
            if v in nums:
                nums[v] += 1
            else:
                nums[v] = 1
        elif cmd[0] == 'D':
            if int(cmd[1]) == 1: #최댓값
                while max_hq:
                    v = -heapq.heappop(max_hq)
                    if v in nums:
                        nums[v] -= 1
                        if nums[v] == 0:
                            del(nums[v])
                        break
            else:
                while min_hq:
                    v = heapq.heappop(min_hq)
                    if v in nums:
                        nums[v] -= 1
                        if nums[v] == 0:
                            del(nums[v])
                        break
                    
     # 출력 전 heap 정리
    while max_hq:
        v = -max_hq[0]
        if v in nums:
            break
        heapq.heappop(max_hq)

    while min_hq:
        v = min_hq[0]
        if v in nums:
            break
        heapq.heappop(min_hq)

    if max_hq and min_hq:
        print(-heapq.heappop(max_hq),heapq.heappop(min_hq))
    else:
        print('EMPTY')