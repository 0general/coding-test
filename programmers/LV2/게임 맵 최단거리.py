from collections import deque

# 명규의 마리오네트


def solution(maps):
    # 현재 노드 위치
    x = 0
    y = 0
    # 이동방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 행렬 크기
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = deque()

    queue.append([0, 0, 1])
    visited[0][0] = True

    while queue:
        x, y, c = queue.popleft()  # c = x,y 좌표에 도달하기까지 경로
        if x == n-1 and y == m-1:
            return c
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx == -1 or ty == -1 or tx == n or ty == m:
                continue
            if maps[tx][ty] == 1 and visited[tx][ty] == False:
                queue.append([tx, ty, c+1])
                visited[tx][ty] = True

    return -1
