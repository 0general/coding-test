import re
from collections import Counter
from itertools import permutations as pm


def solution(expression):
    c = ['*', '+', '-']
    d = dict()
    result = []
    onum = re.split(r'\D', expression)
    e = re.split(r'[\d]+', expression)
    e = e[1:len(e)-1]
    esu = Counter(e)
    for i, j in enumerate(e):
        onum.insert((i*2+1), j)
    for k in list(pm(c, 3)):
        num = onum
        for a, b in zip(range(3), k):
            d[a] = b

        for ii in range(3):
            if esu[d[ii]] == 0:
                continue
            for i in range(esu[d[ii]]):
                t = []
                id = num.index(d[ii])
                t = num[:id-1]
                if d[ii] == '*':
                    t.append(int(num[id-1])*int(num[id+1]))
                elif d[ii] == "+":
                    t.append(int(num[id-1])+int(num[id+1]))
                else:
                    t.append(int(num[id-1])-int(num[id+1]))
                if id+1 == len(num)-1:
                    num = t
                    break
                else:
                    t += num[id+2:]
                    num = t

        result.append(abs(num[0]))
    return max(result)
