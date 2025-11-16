n = int(input())
arr = []

for i in range(n):
    value = int(input())
    if value != 0:
        arr.append(value)
    else:
        arr.pop()

print(sum(arr))