"""
https://www.acmicpc.net/problem/17822
"""
import sys
from collections import deque
input = sys.stdin.readline

# 원판 개수, 각 원판에 적힌 정수 수, 회전 수
n, m, t = map(int, input().split())

# 원판에 남아있는 정수의 총 개수
num = m*n
c_num = [m]*n


# 원판
circle = [deque(map(int, input().split())) for _ in range(n)]


# 회전
def rotate(idx, d, k):
    global n, m, circle, c_num
    k %= m
    if d == 1:
        k = -k
    i = 1
    # 배수 원판도 처리
    while idx*i <= n:  # 사실 i = idx로 두고 i += idx로 처리했어도 된다.
        x = idx*i - 1
        if c_num[x] != 0:
            circle[x].rotate(k)
        i += 1


# 인접 동일 숫자 삭제
def bfs():
    global n, m, circle, num, c_num
    # 인접한게 존재하지 않으면 평균 계산도 해야 함
    adj = False
    visited = [[False]*m for _ in range(n)]
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 전체 원판의 숫자를 모두 확인
    for i in range(n):
        for j in range(m):
            # 숫자가 빈 곳은 볼 필요 없음
            if circle[i][j] == 0:
                continue
            if not visited[i][j]:  # 0이 아닌 것들 중에 인접 체크
                clear = False  # i,j를 지워도 되는가 = 인접한 동일 숫자가 있으면 지워야 한다.
                q = deque()
                check = circle[i][j]
                visited[i][j] = True
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in dir:
                        nx, ny = x+d[0], y+d[1]
                        if nx < 0 or nx >= n:
                            continue
                        if c_num[nx] == 0:
                            continue
                        if ny < 0:
                            ny = m-1
                        if ny >= m:
                            ny = 0
                        if not visited[nx][ny] and circle[nx][ny] == check:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            # 원판 위에 남은 정수의 개수 계산
                            circle[nx][ny] = 0
                            c_num[nx] -= 1
                            num -= 1
                            clear = True  # 인접한게 존재함
                if clear:
                    circle[i][j] = 0
                    c_num[i] -= 1
                    num -= 1
                    adj = True
    if not adj:
        mean()

# 원판의 숫자 합


def circle_sum():
    global n, m, circle, num
    hap = 0
    for i in range(n):
        hap += sum(circle[i])

    return hap


# 평균 계산해서 큰 숫자, 작은 숫자 줄이고 늘리기
def mean():
    global n, m, circle, num
    if num == 0:
        return
    hap = circle_sum()
    m_num = hap/num
    for i in range(n):
        for j in range(m):
            # 빈 곳은 무시
            if circle[i][j] == 0:
                continue
            elif circle[i][j] > m_num:
                circle[i][j] -= 1
            elif circle[i][j] < m_num:
                circle[i][j] += 1


for _ in range(t):
    xi, d, k = map(int, input().split())
    rotate(xi, d, k)
    bfs()

print(circle_sum())
