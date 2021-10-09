"""
https://www.acmicpc.net/problem/6603
"""
import sys
from itertools import combinations
input = sys.stdin.readline


while True:
    t = list(map(int, input().split()))
    if t[0] == 0:
        break

    k = t[0]
    t = sorted(t[1:])

    for st in combinations(t, 6):
        for i in st:
            print(i, end=" ")
        print()

    print()
