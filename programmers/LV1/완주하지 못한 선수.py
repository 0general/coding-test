
# 더 간결한 풀이
from collections import Counter


def solution2(participant, completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]


'''
# 나의 풀이
-------------------------------------------------------------------------------------------------
'''


def solution(participant, completion):
    answer = ''
    key = set(completion)
    dict = {}
    a = set(participant)
    if len(a) != len(key):
        b = a - key
        return b.pop()
    else:  # 동명이인
        participant.sort()
        completion.sort()
        for i in range(len(completion)):
            if participant[i] != completion[i]:
                return participant[i]
            elif i == len(completion)-1 and participant[i] == completion[i]:
                return participant[i]
    return answer
