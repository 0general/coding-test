"""
https://www.acmicpc.net/problem/7562
"""
import sys
from collections import deque

input = sys.stdin.readline
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())
for _ in range(t):
    I = int(input())
    visit = [[False]*I for _ in range(I)]
    x, y = map(int, input().split())
    d_x, d_y = map(int, input().split())
    q = deque()
    cnt = 0
    if (x, y) == (d_x, d_y):
        print(cnt)
        continue
    visit[x][y] = True
    q.append((x, y, cnt))
    while q:
        i, j, num = q.popleft()
        for k in range(len(dx)):
            ni, nj = i+dx[k], j+dy[k]
            if 0 <= ni < I and 0 <= nj < I and not visit[ni][nj]:
                if (ni, nj) == (d_x, d_y):
                    print(num+1)
                    break
                visit[ni][nj] = True
                q.append((ni, nj, num+1))
        else:
            continue
        break
