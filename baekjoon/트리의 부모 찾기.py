"""
https://www.acmicpc.net/problem/11725
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
p = [0]*(n+1)

arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)
while q:
    now = q.popleft()
    for i in arr[now]:
        if p[i] == 0:
            p[i] = now
            q.append(i)

for i in p[2:]:
    print(i)
