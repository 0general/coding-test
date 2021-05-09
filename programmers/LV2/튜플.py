'''
깔끔한 다른 코드
https://programmers.co.kr/learn/courses/30/lessons/64065/solution_groups?language=python3
'''

import re


def solution(s):
    answer = []
    b = re.split('{|}', s)
    while '' in b:
        b.remove('')
    while ',' in b:
        b.remove(',')
    b.sort(key=len, reverse=True)

    for i in range(-1, -len(b)-1, -1):
        if i == -1:
            answer.append(int(b[i]))
        else:
            c = re.split(',', b[i])
            d = re.split(',', b[i+1])
            temp = set(c)-set(d)
            answer.append(int(temp.pop()))
    return answer
