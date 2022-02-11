"""
https://www.acmicpc.net/problem/2056
"""
# 위상정렬 문제

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
ls = [[] for _ in range(n+1)]
working_time = [0]*(n+1)
delay_time = [0]*(n+1)
indegree = [0]*(n+1)
q = deque()

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    working_time[i] = arr[0]
    if arr[1] == 0:
        q.append(i)
        delay_time[i] = working_time[i]
        continue
    num = 0
    for j in arr[2:]:
        ls[j].append(i)
        num += 1
    indegree[i] = num


while q:
    now = q.popleft()
    for k in ls[now]:
        delay_time[k] = max(delay_time[k], delay_time[now] + working_time[k])
        indegree[k] -= 1
        if indegree[k] == 0:
            q.append(k)

print(max(delay_time))
