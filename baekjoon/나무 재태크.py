"""
https://www.acmicpc.net/problem/16235
"""
import sys

input = sys.stdin.readline

# 땅 크기, 나무의 개수, k년
N, M, K = map(int, input().split())

# A배열 입력
A = [list(map(int, input().split())) for _ in range(N)]
Map = [[5]*N for _ in range(N)]  # 현재 땅 위치별
tree = [[] for _ in range(K+11)]  # 살아있는 나무들의 나이별 위치
for _ in range(M):
    # 심은 나무 M개의 정보 x,y 위치, z는 나무의 나이
    x, y, z = map(int, input().split())
    tree[z].append((x-1, y-1))

dtree = []  # 죽은 나무들의 위치 저장


# 봄
def spring():
    global tree, dtree, Map
    # 1. 나이만큼 어린 나무부터 양분 먹기
    next = [[] for _ in range(len(tree))]
    for z in range(1, len(tree)):
        for _ in range(len(tree[z])):
            x, y = tree[z].pop()
            # 2. 나이 증가 + 5의 배수가 되면 fall 부름
            if Map[x][y] >= z:
                Map[x][y] -= z
                next[z+1].append((x, y))
                if (z+1) % 5 == 0:
                    next = fall(x, y, next)
            else:
                # 3. 나무의 죽음
                dtree.append((x, y, z))
    tree = next
    return


# 여름
def summer():  # 죽은 나무 큐 받음
    global dtree, Map
    # 나무의 양분화 죽은 나무마다 나이를 //2한 값이 땅의 양분으로 추가
    while dtree:
        x, y, z = dtree.pop()
        Map[x][y] += (z//2)
    return


# 가을
def fall(x, y, next):  # 번식하는 나무의 위치
    global N
    # 1. 나이가 5의 배수인 나무만 들어올거니까 나무 나이 신경 ㄴㄴ
    # 2. 땅을 벗어나지 않는 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
    for d in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (1, 1), (-1, 1)]:
        nx, ny = x+d[0], y+d[1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        next[1].append((nx, ny))
    return next


# 겨울
def winter():
    global N, Map, A
    # 땅에 A[r][c]만큼 양분 추가
    for r in range(N):
        for c in range(N):
            Map[r][c] += A[r][c]


# K년이 지난 후 땅에 살아있는 나무의 개수를 구하자
for _ in range(K):
    spring()
    summer()
    winter()

num = 0
for i in range(1, len(tree)):
    num += len(tree[i])

print(num)
