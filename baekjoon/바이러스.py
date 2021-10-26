"""
https://www.acmicpc.net/problem/2606
"""
from collections import deque
c = int(input())  # 컴퓨터 수
n = int(input())  # 연결된 컴퓨터 쌍 수
network = [[] for _ in range(c)]
visited = [False]*c
q = deque()

for _ in range(n):
    a, b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)

cnt = 0
network = list(map(sorted, network))

visited[0] = True
q.append(0)

while q:
    now = q.popleft()
    for computer in network[now]:
        if not visited[computer]:
            visited[computer] = True
            q.append(computer)
            cnt += 1

print(cnt)
