a = list(map(int,input().split()))
N = a[0]
arr = a[1:]
while len(arr) < N:
    a = list(map(int,input().split()))
    arr.extend(a)

rev = []
for x in arr:
    reversed_num = int(str(x)[::-1])
    rev.append(reversed_num)

rev.sort()
for x in rev:
    print(x)