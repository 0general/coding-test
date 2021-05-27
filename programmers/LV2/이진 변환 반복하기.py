from collections import Counter


def solution(s):
    answer = [0, 0]
    while len(s) != 1:
        answer[0] += 1
        answer[1] += Counter(s)['0']
        s = str(bin(Counter(s)['1'])[2:])
    return answer
