import math


def solution(brown, yellow):
    n = int(math.sqrt(yellow))

    for y in range(1, n+1):
        if yellow % y == 0:
            x = int(yellow/y)
            if (2*x+2*y + 4) == brown:
                return [x+2, y+2]
