n = int(input())

for x in range(max(0,n-10*len(str(n))),n):
    if x + sum(map(int, str(x))) == n:
        print(x)
        break
else:
    print('0')