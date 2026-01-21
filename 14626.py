isbn = input().strip()
cnt = 0
weight = 1

for i in range(13):
    if isbn[i] != '*':
        if i % 2 == 0:
            cnt += int(isbn[i])
        else:
            cnt += 3 * int(isbn[i])
    else:
        weight = 1 if i % 2 == 0 else 3

for x in range(10):
    if (cnt + x * weight) % 10 == 0:
        print(x)
        break