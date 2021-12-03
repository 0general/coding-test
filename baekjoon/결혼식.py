"""
https://www.acmicpc.net/problem/5567
"""
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
q = deque()
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        visited[b] = True
        q.append(b)  # 친구들이 모두 들어감
        answer += 1
    else:
        graph[a].append(b)
        graph[b].append(a)

while q:  # 친구의 친구 처리
    f = q.popleft()
    for i in graph[f]:
        if not visited[i]:
            visited[i] = True
            answer += 1

print(answer)
