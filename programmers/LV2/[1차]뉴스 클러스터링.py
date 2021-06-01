import re
from collections import Counter


def solution(str1, str2):
    str1 = re.findall(r"[A-Z]+", str1.upper())
    str2 = re.findall(r"[A-Z]+", str2.upper())
    d1 = []
    d2 = []
    if not len(str1) and not len(str2):
        return 65536
    elif not len(str1) or not len(str2):
        return 0
    for i in str1:
        if len(i) < 2:
            continue
        for j in range(len(i)-1):
            d1.append(i[j:j+2])
    for i in str2:
        if len(i) < 2:
            continue
        for j in range(len(i)-1):
            d2.append(i[j:j+2])
    d1 = Counter(d1)
    d2 = Counter(d2)
    gyo = len(list((d1 & d2).elements()))
    hap = len(list(((d1+d2)-(d1 & d2)).elements()))
    if not gyo and not hap:
        return 65536
    elif not gyo:
        return 0
    return int((gyo/hap)*65536)
