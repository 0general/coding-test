from itertools import combinations
import math


def solution(nums):
    check = [sum(x) for x in combinations(nums, 3)]
    answer = 0

    for i in check:
        prime_ok = True
        su = int(math.sqrt(i))
        for j in range(2, su+1):
            if i % j == 0:
                prime_ok = False
                break
        if not prime_ok:
            continue
        answer += 1

    return answer
