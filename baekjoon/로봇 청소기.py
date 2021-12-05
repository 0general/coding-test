"""
https://www.acmicpc.net/problem/14503
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())  # 현재 위치와 방향
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]

clear = 0  # 청소한 칸의 개수

while True:
    if not visited[r][c]:  # 청소를 안 했다면 청소
        visited[r][c] = True
        clear += 1
    for _ in range(4):
        d = (d-1) % 4  # 현재 방향 기준 왼쪽으로 먼저 회전
        nr, nc = r+dx[d], c+dy[d]  # 그 방향으로 직진 (가능성)
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0 and not visited[nr][nc]:
            r, c = nr, nc  # 청소하지 않은 빈 칸이 존재하면 직진
            break
    else:  # 4방향 모두 갈 곳이 없는 상태일 때 (for문에서 break에 걸리면 실행 안 함)
        nr, nc = r-dx[d], c-dy[d]  # for문을 4번 돌아서 원래 방향. 뒤로 후진
        # 범위 내에 존재, 벽이 아님
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
            r, c = nr, nc  # 방향 그대로 가지고 이동
        else:
            break

print(clear)
