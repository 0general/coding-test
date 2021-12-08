"""
https://www.acmicpc.net/problem/1918
"""
import sys

input = sys.stdin.readline
tokenList = input().rstrip()

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}


opStack = []
answer = ''
for token in tokenList:
    if token == "(":
        opStack.append(token)
    elif token == ")":
        while opStack[-1] != "(":
            answer += opStack.pop()
        opStack.pop()
    elif token in prec:  # 연산자일 때
        while len(opStack) > 0 and prec[opStack[-1]] >= prec[token]:
            answer += opStack.pop()
        opStack.append(token)
    else:  # 피연산자일 때
        answer += token
while len(opStack):
    answer += opStack.pop()

print(answer)
