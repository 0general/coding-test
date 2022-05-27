"""
https://www.acmicpc.net/problem/16234
"""
import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ok = True


def people_move(ls, num):
    global arr
    x = num // len(ls)
    while ls:
        i, j = ls.pop()
        arr[i][j] = x


def find_unit():
    global ok
    visited = [[False]*N for _ in range(N)]
    q = deque()
    ls = []

    for i in range(N):
        for j in range(N):
            ls = []
            num = 0
            if not visited[i][j]:
                visited[i][j] = True
                num += arr[i][j]
                q.append((i, j))
                ls.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in dir:
                        nx, ny = x + d[0], y + d[1]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                            continue
                        if L <= abs(arr[nx][ny]-arr[x][y]) <= R:
                            num += arr[nx][ny]
                            visited[nx][ny] = True
                            ls.append((nx, ny))
                            q.append((nx, ny))
                if len(ls) == 1:
                    continue
                people_move(ls, num)
                ok = True


day = 0
while ok:
    ok = False
    find_unit()
    if ok:
        day += 1

print(day)
