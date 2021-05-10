from collections import Counter
from collections import deque


def check(p, answer):
    u = ''
    v = ''

    right = True

    for i, j in enumerate(p):
        u += j
        if Counter(u)['('] == Counter(u)[')'] and i != len(p)-1:
            v = p[i+1:]
            break
    print('u = ', u)
    print('v = ', v)
    que = deque(u)
    cnt = 0

    while que:
        if que.popleft() == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                right = False
                break
    print(right)
    if right:
        answer += "".join(u)
        if v != "":
            answer = check(v, answer)
    else:
        bin = "("
        bin += check(v, "")
        bin += ")"
        print('bin = ', bin)
        u = u[1:len(u)-1]
        for i in u:
            if i == "(":
                bin += ")"
            else:
                bin += "("
        print('bin = ', bin)
        return answer + bin
    return answer


def solution(p):
    answer = ''
    answer = check(p, answer)
    return answer
