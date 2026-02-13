X, Y, W, S = map(int, input().split())

if 2 * W <= S:
    print((X + Y) * W)
elif S < W:
    if (X + Y) % 2 == 0:
        print(max(X, Y) * S)
    else:
        print((max(X, Y) - 1) * S + W)
else:
    print(min(X, Y) * S + abs(X - Y) * W)