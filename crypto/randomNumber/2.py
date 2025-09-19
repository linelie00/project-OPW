def linear_congruence_method(a, c, m, seed, max=50):
    result = []
    r = seed

    for _ in range(max):
        r = (a * r + c) % m
        result.append(r)

    for i in range(1, len(result) // 2 + 1):
        pattern = result[:i]
        count = 0

        for j in range(0, len(result) - i + 1, i):
            if result[j:j+i] == pattern:
                count += 1
            else:
                break

        if count >= 3:
            return result, pattern

    return result, []

A = int(input("A: "))
C = int(input("C: "))
M = int(input("M: "))
Seed = int(input("Seed: "))


sequence, cycle = linear_congruence_method(A, C, M, Seed)


print("생성된 난수열:", sequence)
print("주기:", cycle)
print("주기 길이:", len(cycle) if cycle else "없음")

