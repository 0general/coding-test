"""
https://www.acmicpc.net/problem/14867
"""
from collections import deque

a, b, c, d = map(int, input().split())

if c == 0 and d == 0:
    print(0)
else:
    visited = [[False]*(b+1) for _ in range(a+1)]
    ans = -1
    visited[0][0] = True
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, t = q.popleft()
        for nx, ny in [(a, y), (x, b), (x, 0), (0, y), (a, x+y-a), (x+y, 0), (x+y-b, b), (0, x+y)]:
            if 0 <= nx <= a and 0 <= ny <= b and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, t+1))
                if nx == c and ny == d:
                    ans = t+1
                    break
        else:
            continue
        break
    print(ans)
