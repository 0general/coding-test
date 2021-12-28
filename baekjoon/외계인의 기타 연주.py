"""
https://www.acmicpc.net/problem/2841
자료 구조 stack
"""
import sys

input = sys.stdin.readline

n, p = map(int, input().split())
count = 0

line = [[] for _ in range(n+1)]

for _ in range(n):
    l, f = map(int, input().split())
    while True:
        if len(line[l]) == 0:
            line[l].append(f)
            count += 1
            break
        if line[l][-1] > f:
            line[l].pop()
            count += 1
        elif line[l][-1] == f:
            break
        else:
            line[l].append(f)
            count += 1
            break

print(count)
