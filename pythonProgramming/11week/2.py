#주어진 정수의 각 자릿수의 합을 구하는 재귀함수
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

i = int(input())
print(sum_digits(i))