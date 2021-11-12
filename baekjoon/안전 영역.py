"""
https://www.acmicpc.net/problem/2468
"""
import sys
from collections import deque


def bfs():  # h보다 큰 지역 수
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i+dx[k], j+dy[k]
            if 0 <= x < n and 0 <= y < n and graph[x][y] > h and not visit[x][y]:
                visit[x][y] = True
                q.append((x, y))


input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

q = deque()
ans = 1  # 강수량이 0일 때

for h in range(1, 101):  # 강수량
    visit = [[False]*n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if h < graph[i][j] and not visit[i][j]:  # 물에 잠기지 않는 영역을 구한다.
                temp += 1
                visit[i][j] = True
                q.append((i, j))
                bfs()
    if temp == 0:  # 물에 잠기지 않는 영역 수가 0이면 for문 탈출
        break
    ans = max(ans, temp)

print(ans)
