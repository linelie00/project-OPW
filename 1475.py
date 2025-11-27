n = list(map(int, input()))
arr = [0 for _ in range(9)]
for i in n:
    if i == 9:
        arr[6] += 1
    else: arr[i] += 1
arr[6] = (arr[6]+1)//2
print(max(arr))