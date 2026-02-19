expr = input().strip()

parts = expr.split('-')

answer = sum(map(int, parts[0].split('+')))

for p in parts[1:]:
    answer -= sum(map(int, p.split('+')))

print(answer)