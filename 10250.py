t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y = (n - 1) % h + 1     # 층
    x = (n - 1) // h + 1    # 호수
    print(y * 100 + x)
