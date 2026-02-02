def digit_sum(x: str) -> int:
    return sum(int(ch) for ch in x if ch.isdigit())

n = int(input())
arr = [input().strip() for _ in range(n)]

arr.sort(key=lambda x: (len(x), digit_sum(x), x))

for x in arr:
    print(x)