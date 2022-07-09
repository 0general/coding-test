"""
https://www.acmicpc.net/problem/12851
"""
import sys
from collections import deque
input = sys.stdin.readline
q = deque()
n, k = map(int, input().split())
visited = [-1]*100001  # 방문한 시간 기록
num = [0]*100001  # 방문한 횟수 기록

visited[n] = 0
num[n] = 1
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        break
    for nx in [x+1, x-1, 2*x]:
        if nx < 0 or nx > 100000:
            continue
        if visited[nx] < 0:
            visited[nx] = visited[x]+1
            num[nx] = num[x]
            q.append(nx)
        else:
            if visited[nx] == visited[x]+1:  # 이미 방문을 했더라도 횟수를 기록해줘야 한다.
                num[nx] += num[x]

print(visited[k])
print(num[k])
