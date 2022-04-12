"""
https://www.acmicpc.net/problem/9177
"""
import sys
from collections import deque

input = sys.stdin.readline

# 재귀로 같은 로직을 썼을 때는 visited 처리를 안 해줘서 시간초과가 났었다.


def bfs():
    a, b, c = input().rstrip().split(' ')
    visited = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    q = deque()
    visited[0][0] = True
    q.append((0, 0, 0))

    while q:
        x, y, z = q.popleft()
        if x == len(a) and y == len(b) and z == len(c):
            return True
        if x < len(a) and a[x] == c[z] and not visited[x+1][y]:
            visited[x+1][y] = True
            q.append((x+1, y, z+1))
        if y < len(b) and b[y] == c[z] and not visited[x][y+1]:
            visited[x][y+1] = True
            q.append((x, y+1, z+1))

    return False


for num in range(1, int(input())+1):
    if bfs():
        print(f"Data set {num}: yes")
    else:
        print(f"Data set {num}: no")
