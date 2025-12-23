import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()), reverse=True)
b = sorted(map(int, input().split()))

print(sum(a[i] * b[i] for i in range(n)))