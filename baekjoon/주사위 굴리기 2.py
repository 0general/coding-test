"""
https://www.acmicpc.net/problem/23288
2021 삼성 하반기 공채 오전 코딩테스트 1번 문제 기출
"""
from collections import deque


def bfs(r, c):  # board 점수판 미리 계산
    num = board[r][c]
    ls = []
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        ls.append((r, c))
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < n and 0 <= dc < m and not visited[dr][dc] and board[dr][dc] == num:
                visited[dr][dc] = True
                q.append((dr, dc))
    return ls, cnt * num


# 세로, 가로, 이동 횟수
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score_board = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        score_board[i][j] = board[i][j]
visited = [[False]*m for _ in range(n)]
dir = 0  # 초기 방향 = 오른쪽 방향
q = deque()
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]

# 진행 방향에 따른 주사위 상태 변화
# 0 : 오른쪽, 1: 아래쪽, 2:왼쪽, 3: 위쪽
dice_state = [[3, 1, 0, 5, 4, 2],
              [1, 5, 2, 3, 0, 4],
              [2, 1, 5, 0, 4, 3],
              [4, 0, 2, 3, 5, 1]]

# 주사위가 멈췄을 경우 얻게 될 점수 미리 계산
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))
            ls, score = bfs(i, j)
            for idx in ls:
                score_board[idx[0]][idx[1]] = score

state = [1, 2, 3, 4, 5, 6]
ans_score = 0  # 출력할 최종 점수
x, y = 0, 0  # 초기 위치
for _ in range(k):  # 게임 턴 수
    # 주사위 이동 -> 현재 위치 갱신
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m:
        x = nx
        y = ny
    else:
        dir = dir ^ 2
        x += dx[dir]
        y += dy[dir]
    # 주사위 상태
    new_state = []
    for i in dice_state[dir]:
        new_state.append(state[i])
    state = new_state
    # 점수 획득
    ans_score += score_board[x][y]
    # 다음 방향 확정
    if state[5] > board[x][y]:
        dir += 1
    elif state[5] < board[x][y]:
        dir -= 1
    dir %= 4

print(ans_score)
