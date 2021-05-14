from itertools import combinations
from collections import Counter


def solution(numbers, target):
    full = sum(numbers)
    if full == target:
        return 1
    if -full == target:
        return 1
    minus = (full - target)//2
    hap = []
    for i in range(1, len(numbers)):
        hap.extend(list(map(sum, combinations(numbers, i))))
    result = Counter(hap)
    if minus in result:
        return result[minus]
    return 0
