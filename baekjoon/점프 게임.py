"""
https://www.acmicpc.net/problem/15558
"""
import sys
from collections import deque


input = sys.stdin.readline
n, k = map(int, input().split())
graph = [[0]+list(map(int, list(input().rstrip()))) for _ in range(2)]
visited = [[False]*(n+1) for _ in range(2)]
dx = [0, 0, -1, 1]
dy = [1, -1, k, k]
q = deque()
flag = False

visited[0][1] = True
q.append((0, 1, 0))

while q:
    x, y, cnt = q.popleft()  # 현재 위치 현재 초
    for i in range(len(dx)):
        nx, ny = x+dx[i], y+dy[i]
        # cnt는 이동 횟수이자 초. cnt초에 다음으로 이동할 위치는 떠남과 동시에 사라질 위치인 cnt인덱스보다 커야 한다.
        if 0 <= nx < 2 and cnt+1 < ny:
            if ny > n: # 이 조건 중요 이거 안 해줘서 3번 틀림
                flag = True
                break
            elif graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 체크
                if ny == n:
                    flag = True
                    break
                q.append((nx, ny, cnt + 1))

if flag:
    print(1)
else:
    print(0)
