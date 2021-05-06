from collections import Counter


def solution(nums):
    n = len(nums)//2
    type = Counter(nums)
    if n >= len(type):
        answer = len(type)
    else:
        answer = n

    return answer
