import numpy as np
import math


def solution(progresses, speeds):
    pg = np.array(progresses)
    sp = np.array(speeds)
    def plus(x): return 100 - x
    day = list(map(plus, pg))
    day = np.array(day)/sp
    day = list(map(math.ceil, day))
    answer = []
    stack = []
    com = day[0]
    for i in day:
        if i <= com:
            stack.append(i)
        else:
            answer.append(len(stack))
            stack.clear()
            com = i
            stack.append(i)
    answer.append(len(stack))
    return answer
