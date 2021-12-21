"""
https://www.acmicpc.net/problem/12869
"""
from collections import deque
from itertools import permutations as pm
import sys

input = sys.stdin.readline
N = int(input())
SCN = list(map(int, input().split()))
visited = [[[False]*61 for _ in range(61)] for _ in range(61)]

d = {0: 9, 1: 3, 2: 1}

q = deque()
q.append((SCN, 0))
flag = 0

while q:
    now, t = q.popleft()
    for p in pm(now, N):
        ls = list(p)
        for i in range(N):
            ls[i] = max(0, ls[i]-d[i])
        ls.sort(reverse=True)
        a = ls[0]
        b = ls[1] if N >= 2 else 0
        c = ls[2] if N >= 3 else 0
        if a == 0 and b == 0 and c == 0:
            flag = t+1
            break
        if not visited[a][b][c]:
            visited[a][b][c] = True #반드시 잊지말고 챙길 것. 안 챙겼다가 두 번 틀림
            q.append((ls, t+1))
    if flag != 0:
        break

print(flag)
