"""
https://www.acmicpc.net/problem/14867
"""
# 기본 BFS로 43점만 받아 부분 성공 고쳐야 함 -> 메모리 고려 안 함
# 10만 * 10만 배열로 방문처리를 하면 터진다.

from collections import deque

a, b, c, d = map(int, input().split())

visited = set()
ans = -1
visited.add((0, 0))
q = deque()
q.append((0, 0, 0))
while q:
    x, y, t = q.popleft()
    if x == c and y == d:
        ans = t
        break
    for nx, ny in [(a, y), (x, b), (x, 0), (0, y)]:
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny, t+1))
    if a-x >= y and (x+y, 0) not in visited:
        visited.add((x+y, 0))
        q.append((x+y, 0, t+1))
    elif a-x < y and (a, x+y-a) not in visited:
        visited.add((a, x+y-a))
        q.append((a, x+y-a, t+1))
    if b-y >= x and (0, x+y) not in visited:
        visited.add((0, x+y))
        q.append((0, x+y, t+1))
    elif b-y < x and (x+y-b, b) not in visited:
        visited.add((x+y-b, b))
        q.append((x+y-b, b, t+1))

print(ans)
