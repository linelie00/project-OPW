#후위표기식
#https://www.acmicpc.net/problem/1918

v = list(input())
stack = []

priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 0
}

for i in v:
    if i.isalpha():
        print(i, end="")
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end="")
        stack.pop()
    else:
        while stack and priority[stack[-1]] >= priority[i]:
            print(stack.pop(), end="")
        stack.append(i)
print(''.join(reversed(stack)))