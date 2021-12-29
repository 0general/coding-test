"""
https://www.acmicpc.net/problem/2251
"""
from collections import deque

A, B, C = map(int, input().split())
visited = [[[False]*(C+1) for _ in range(B+1)] for _ in range(A+1)]

q = deque()
visited[0][0][C] = True
water = [False]*(C+1)
water[C] = True

q.append((0, 0, C))
while q:
    a, b, c = q.popleft()
    n = a + b
    if n <= B:  # a -> b
        if not visited[0][n][c]:
            visited[0][n][c] = True
            q.append((0, n, c))
            if not water[c]:
                water[c] = True
    else:
        if not visited[n-B][B][c]:
            visited[n-B][B][c] = True
            q.append((n-B, B, c))
    if n <= A:  # b -> a
        if not visited[n][0][c]:
            visited[n][0][c] = True
            q.append((n, 0, c))
            if n == 0 and not water[c]:
                water[c] = True
    else:
        if not visited[A][n-A][c]:
            visited[A][n-A][c] = True
            q.append((A, n-A, c))
    n = b + c
    if not visited[a][0][n]:  # b -> c
        visited[a][0][n] = True
        q.append((a, 0, n))
        if a == 0 and not water[n]:
            water[n] = True
    if n <= B:  # c -> b
        if not visited[a][n][0]:
            visited[a][n][0] = True
            q.append((a, n, 0))
            if a == 0 and not water[0]:
                water[0] = True
    else:
        if not visited[a][B][n-B]:
            visited[a][B][n-B] = True
            q.append((a, B, n-B))
            if a == 0 and not water[n-B]:
                water[n-B] = True
    n = a+c
    if not visited[0][b][n]:  # a -> c
        visited[0][b][n] = True
        q.append((0, b, n))
        if not water[n]:
            water[n] = True
    if n <= A:  # c -> a
        if not visited[n][b][0]:
            visited[n][b][0] = True
            q.append((n, b, 0))
            if n == 0 and not water[0]:
                water[0] = True
    else:
        if not visited[A][b][n-A]:
            visited[A][b][n-A] = True
            q.append((A, b, n-A))


for i in range(C+1):
    if water[i]:
        print(i, end=' ')
