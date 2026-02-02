import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
s = [int(input().strip()) for _ in range(n)]
mode = Counter(s)
max = max(mode.values())
print(min(s for s,v in mode.items() if v == max))