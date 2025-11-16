n = int(input())
a = 1

for i in range(n):
    n = n - a
    if n <= 0:
        print(i + 1)
        break
    a += 6
    if i == 0:
        a = 6