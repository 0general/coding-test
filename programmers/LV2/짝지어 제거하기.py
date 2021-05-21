def solution(st):
    s = list(st)
    stack = []
    top = -1
    for i in range(len(s)):
        if top == -1:
            stack.append(s[i])
            top += 1
        else:
            if s[i] == stack[-1]:
                stack.pop()
                top -= 1
            else:
                stack.append(s[i])
                top += 1

    if len(stack) != 0:
        return 0
    return 1
