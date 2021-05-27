from collections import deque


def solution(priorities, location):
    lc = deque(range(len(priorities)))
    pr = deque(priorities)
    n = len(priorities)

    while location in lc:
        l = lc.popleft()
        g = pr.popleft()
        for i in pr:
            if i > g:
                pr.append(g)
                lc.append(l)
                break
        answer = n - len(pr)

    return answer
