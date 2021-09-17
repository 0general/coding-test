'''
https://www.acmicpc.net/problem/15650
'''
from itertools import combinations

n, m = map(int, input().split())
arr = list(combinations(range(1, n+1), m))

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
