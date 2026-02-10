L, C = map(int, input().split())
arr = sorted(input().split())

def solution(idx, crypt, v, l):
    if l == L:
        if v >= 1 and L - v >= 2:
            print(''.join(crypt))
        return
    if idx == C:
        return

    nv = v + 1 if arr[idx] in 'aeiou' else v
    solution(idx + 1, crypt + [arr[idx]], nv, l + 1)

    solution(idx + 1, crypt, v, l)

solution(0, [], 0, 0)