"""
https://www.acmicpc.net/problem/14248
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
visited = [False]*n
s = int(input()) - 1

ans = 1

visited[s] = True
q = deque()
q.append(s)

while q:
    now = q.popleft()
    x = arr[now]
    for i in (now-x, now+x):
        if i < 0 or i >= n or visited[i]:
            continue
        visited[i] = True
        ans += 1
        q.append(i)

print(ans)
