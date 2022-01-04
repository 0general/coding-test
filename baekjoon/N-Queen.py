"""
https://www.acmicpc.net/problem/9663
"""
# import time
# 참고 : https://zidarn87.tistory.com/339 -> 시간 초과
#answer1 = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]


def check(x, y, num):
    for i in range(1, n-x):
        if 0 <= y-i:
            col[x+i][y-i] += num
        if y+i < n:
            col[x+i][y+i] += num
        col[x+i][y] += num


def BT(x):  # 선택할 행 인덱스이자, 지금까지 선택된 퀸의 개수
    global answer
    if x == n:
        answer += 1
        return
    for i in range(n):
        if col[x][i] == 0:
            check(x, i, 1)
            BT(x+1)  # 다음 행 체크
            check(x, i, -1)


n = int(input())
answer = 0

# 한 행에 반드시 하나를 선택할 수 있어야 n개를 선택할 수 있다.
col = [[0]*n for _ in range(n)]
# s = time.time()
BT(0)
# print(time.time()-s)
# input이 14일 때 150.74167490005493 초가 걸림.

print(answer)
# pypy3로 채점하면 통과된다.
