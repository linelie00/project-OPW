#두 수를 입력받아 지정된 연산을 수행하는 함수를 반환하는 클로저
def calc(i,a,b):
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b
    return {'+':add, '-':sub, '*':mul, '/':div}[i](a,b)

i = input()
a,b = map(int, input().split())
print(calc(i,a,b))