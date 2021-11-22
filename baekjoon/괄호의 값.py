"""
https://www.acmicpc.net/problem/2504
"""


def solution(string):
    stack = []
    pair = {')': '(', ']': '['}
    num = {')': 2, ']': 3}
    l = 0

    if string[-1] in {'(', '['}:  # 여는 괄호로 끝나는 경우는 처음부터 배제
        return 0
    if len(string) % 2 == 1:
        return 0
    for s in string:
        if s == '(' or s == '[':  # 여는 괄호
            stack.append(s)
            l += 1  # 여는 괄호의 숫자
        else:  # 닫는 괄호가 나올 때마다 처리해 줄 것이기에 stack에는 늘 숫자나 여는 괄호만 남아있다.
            c = pair[s]  # ) 이면 (, ] 이면 [
            if len(stack) == 0:
                return 0
            if stack[-1] == c:  # 닫는 괄호의 짝
                stack.pop()
                stack.append(num[s])
                l -= 1
            elif str(stack[-1]).isdigit():
                a = 0
                while str(stack[-1]).isdigit():
                    a += stack.pop()
                    if len(stack) == 0:  # 여는 괄호가 없다는 얘기
                        return 0
                if stack[-1] == c:  # 괄호의 짝이면
                    stack.pop()
                    stack.append(num[s]*a)
                    l -= 1
                else:  # 짝이 맞지 않을 때
                    return 0
            else:  # 짝이 맞지 않을 때
                return 0
    if l != 0:
        return 0
    return sum(stack)  # 숫자만 남음


string = input()
print(solution(string))
