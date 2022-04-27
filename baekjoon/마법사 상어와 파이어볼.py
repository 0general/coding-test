"""
https://www.acmicpc.net/problem/20056
"""
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    r, c = r-1, c-1
    board[r][c].append((m,s,d))


# 파이어볼의 이동 di 방향으로 si%N 만큼
def move():
    global  board
    new_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for _ in range(len(board[i][j])):
                mi,si,di = board[i][j].pop()
                x, y = (i + dir[di][0]*(si%N))%N, (j + dir[di][1]*(si%N)) % N
                new_board[x][y].append((mi,si,di))
    board = new_board

def sum_fireball(i,j):
    global board
    weights = 0
    dir_check = 0
    speed = 0
    while board[i][j]:
        m, s, d = board[i][j].pop()
        weights += m
        dir_check += d % 2
        speed += s
    return weights, dir_check, speed


# 각 칸별 파이어볼 합산이 5 이상일 때, (합산하면서 방향도 같이 홀짝 계산), 새로운 4개로 분할
def magic_fireball():
    global board
    for i in range(N):
        for j in range(N):
            num = len(board[i][j])
            if num <= 1:
                continue
            weights, dir_check, speed = sum_fireball(i,j)
            if weights < 5: # 나눠봤자 무게가 0이라 소멸
                continue
            new_w = weights // 5
            new_s = speed // num
            if dir_check%num: # 방향이 홀짝이 달랐음
                board[i][j] = [(new_w,new_s,1),(new_w,new_s,3),(new_w,new_s,5),(new_w,new_s,7)]
            else:
                board[i][j] = [(new_w, new_s, 0), (new_w, new_s, 2), (new_w, new_s, 4), (new_w, new_s, 6)]


# 전체 파이어볼 합산
def all_fireball():
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += sum_fireball(i,j)[0]
    return ans

# K번 명령
for i in range(K):
    move()
    magic_fireball()

print(all_fireball())
