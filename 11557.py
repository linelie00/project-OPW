t = int(input())
for _ in range(t):
    n = int(input())
    drink = [input().split() for _ in range(n)]
    name, value = max(drink, key=lambda x: int(x[1]))
    print(name)