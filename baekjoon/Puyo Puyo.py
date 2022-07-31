"""
https://www.acmicpc.net/problem/11559
"""
import sys
from collections import deque
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(12)]


def num_check(q, visited):
    stack = []
    while q:
        x, y = q.popleft()
        stack.append((x, y))
        for dir in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    if len(stack) >= 4:
        return stack
    else:
        return []


def bomb(stack):
    if stack:
        while stack:
            i, j = stack.pop()
            arr[i][j] = "."
        fall()


def fall():
    height = [0]*6
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j] == '.':
                continue
            s = arr[i][j]
            arr[i][j] = '.'
            arr[11-height[j]][j] = s
            height[j] += 1


ans = 0
while True:
    visited = [[False]*6 for _ in range(12)]
    bomb_list = []
    q = deque()
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                visited[i][j] = True
                q.append((i, j))
                bomb_list.extend(num_check(q, visited))
    if bomb_list:
        bomb(bomb_list)
        ans += 1
    else:
        break

print(ans)
