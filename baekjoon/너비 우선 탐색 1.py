"""
https://www.acmicpc.net/problem/24444
"""
import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
visited = [0 for _ in range(N+1)]
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

num = 1
visited[R] = num
q = deque()
q.append(R)

while q:
    x = q.popleft()
    arr[x].sort()
    for y in arr[x]:
        if not visited[y]:
            num += 1
            visited[y] = num
            q.append(y)

for i in range(1, N+1):
    print(visited[i])
