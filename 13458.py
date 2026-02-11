N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())
cnt = 0

for i in A:
    cnt += 1
    if i-B >= 0:
        cnt += (i-B+C-1) // C
print(cnt)