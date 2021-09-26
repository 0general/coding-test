"""
https://www.acmicpc.net/problem/10974
"""
from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())

num = sorted(list(permutations(range(1, n+1), n)))

for i in num:
    for j in i:
        print(j, end=' ')
    print()
