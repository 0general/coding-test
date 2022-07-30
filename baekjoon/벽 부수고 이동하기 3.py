"""
https://www.acmicpc.net/problem/16933
"""
# 일반적인 풀이로는 python에서 죽어나는 문제, 메모리를 많이 쓰며 시간 초과가 나기에 가능한 정보를 줄여야 한다.
# 이중 while문과 큐 세 개, 3차원 방문처리를 사용하는 것이, 큐 한 개, 4차원 방문처리를 사용하는 것보다 낫다.
import sys
from collections import deque
input = sys.stdin.readline
ans = -1

N, M, K = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
q1 = deque()
q2 = deque()
q3 = deque()

visited[0][0][0] = 1
q1.append((0, 0, 0, 0))
flag = False

while q1:
    while q1:
        x, y, d, k = q1.popleft()
        num = visited[x][y][k]
        if x == N-1 and y == M-1:
            ans = num
            flag = True
            break
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dir[0], y + dir[1]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if arr[nx][ny] == 1:
                if d == 0 and k < K and not visited[nx][ny][k+1]:
                    visited[nx][ny][k+1] = num + 1
                    q2.append((nx, ny, 1, k+1))
                elif d == 1 and k < K and not visited[nx][ny][k+1]:
                    visited[nx][ny][k+1] = num + 2
                    q3.append((nx, ny, 1, k+1))
            elif arr[nx][ny] == 0 and not visited[nx][ny][k]:
                visited[nx][ny][k] = num + 1
                q2.append((nx, ny, d ^ 1, k))
    if flag:
        break
    q1, q2, q3 = q2, q3, deque()
    if not q1:
        q1, q2 = q2, deque()

print(ans)
