N = int(input())
anw = 0

def dfs(row, arr):
    global anw
    if row == N:
        anw += 1
        return

    for col in range(N):
        ok = True
        for r in range(row):
            if arr[r] == col or abs(arr[r] - col) == row - r:
                ok = False
                break
        if ok:
            dfs(row + 1, arr + [col])

dfs(0, [])
print(anw)