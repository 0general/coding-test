"""
https://www.acmicpc.net/problem/2623
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False]*(N+1)
arr = [[] for _ in range(N+1)]
indeg = [0 for _ in range(N+1)]

for _ in range(M):
    ls = list(map(int, input().split()))
    K = ls[0]
    if K == 0:
        continue
    a = ls[1]
    for x in ls[2:]:
        indeg[x] += 1
        arr[a].append(x)
        a = x

q = deque()
for i in range(1, N+1):
    if indeg[i] == 0:
        visited[i] = True
        q.append(i)

ans = []
while q:
    x = q.popleft()
    ans.append(x)
    for y in arr[x]:
        if visited[y]:
            ans = []
            break
        indeg[y] -= 1
        if indeg[y] == 0:
            visited[y] = True
            q.append(y)
    else:
        continue
    break

if len(ans) == N:
    for x in ans:
        print(x)
else:
    print(0)
