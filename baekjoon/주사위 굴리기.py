"""
https://www.acmicpc.net/problem/14499
"""
import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
dice = [[],
        [0, 4, 2, 1, 6, 5, 3],
        [0, 3, 2, 6, 1, 5, 4],
        [0, 5, 1, 3, 4, 6, 2],
        [0, 2, 6, 3, 4, 1, 5]]
dx = [0, 0, 0, -1, 1]  # 동서북남
dy = [0, 1, -1, 0, 0]
for _ in range(n):
    graph.append(list(map(int, input().rstrip().split())))

ol = list(map(int, input().rstrip().split()))

now = [0, 0, 0, 0, 0, 0, 0]
for o in ol:
    nx, ny = x+dx[o], y + dy[o]
    if 0 <= nx < n and 0 <= ny < m:  # 보드 내에 존재하는가
        x, y = nx, ny  # 주사위 위치 갱신
        temp = [now[dice[o][i]] for i in range(7)]  # 주사위 굴리기
        now = temp
        if graph[x][y] == 0:  # 칸에 쓰여있는 수가 0이면
            graph[x][y] = now[6]  # 주사위 숫자 복사
        else:
            now[6] = graph[x][y]  # 칸 숫자를 주사위에 복사
            graph[x][y] = 0  # 칸 숫자는 0
        print(now[1])
