def is_perfect_number(n):
    total = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            total += i
    return total == n

while True:
    n = int(input())
    
    if n == -1:
        break

    if is_perfect_number(n):
        print(f"{n} = 1 + " + " + ".join(str(i) for i in range(2, n // 2 + 1) if n % i == 0))
    else:
        print(f"{n} is NOT perfect.")
