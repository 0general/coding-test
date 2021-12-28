'''
https://www.acmicpc.net/problem/1325
'''
import sys
from collections import deque

input = sys.stdin.readline

# n은 컴퓨터 수, m은 관계 수
n, m = map(int, input().split())
# i를 신뢰하는 컴퓨터들의 리스트
arr = [[] for _ in range(n+1)]
dp = [0]*(n+1)  # i를 해킹했을 때, 해킹할 수 있는 다른 컴퓨터의 수
hack = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

for i in range(1, n+1):
    visited = [False]*(n+1)
    q = deque()
    visited[i] = True
    q.append(i)
    while q:
        now = q.popleft()
        for k in arr[now]:
            if not visited[k]:
                visited[k] = True
                q.append(k)
                dp[i] += 1
    if len(hack) == 0:
        hack.append(i)
    else:
        if dp[hack[-1]] == dp[i]:
            hack.append(i)
        elif dp[hack[-1]] < dp[i]:
            hack = [i]

print(*hack)
