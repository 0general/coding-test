"""
https://www.acmicpc.net/problem/16940
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
conn = [defaultdict(bool) for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    conn[a][b] = True
    conn[b][a] = True

checklist = list(map(int, input().split()))

if checklist[0] != 1:
    print(0)
else:
    ans = 1
    p_idx = 0
    c_idx = 1
    while c_idx < n:
        if p_idx >= c_idx:
            ans = 0
            break
        if not conn[checklist[p_idx]][checklist[c_idx]]:
            p_idx += 1
            continue
        c_idx += 1
    print(ans)
