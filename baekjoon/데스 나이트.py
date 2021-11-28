"""
https://www.acmicpc.net/problem/16948
"""
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())  # n의 크기
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[False]*n for _ in range(n)]
q = deque()

visited[r1][c1] = True

if r1 == r2 and c1 == c2:
    print(0)
else:
    flag = -1
    q.append((r1, c1, 0))
    while q:
        x, y, cnt = q.popleft()
        for i in range(len(dx)):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if nx == r2 and ny == c2:  # 갱신 조건 == 탈출 조건
                    flag = cnt + 1
                    break
                q.append((nx, ny, cnt+1))
        if flag > 0:  # 갱신되면 무조건 0보다 커진다는 의미
            break
    print(flag)
