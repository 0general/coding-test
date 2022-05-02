"""
https://www.acmicpc.net/problem/2252
위상 정렬
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

e_in = [0]*(n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    e_in[b] += 1
    arr[a].append(b)


q = deque()
for i in range(1, n+1):
    if e_in[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=' ')
    for i in arr[x]:
        if e_in[i] != 0:
            e_in[i] -= 1
        if e_in[i] == 0:
            q.append(i)
