"""
https://www.acmicpc.net/problem/9663
"""
# 참고 : https://zidarn87.tistory.com/339


def check(x):
    for i in range(x):
        if col[x] == col[i] or abs(col[x]-col[i]) == x-i:
            return False
    return True


def BT(x):  # 선택할 행 인덱스이자, 지금까지 선택된 퀸의 개수
    global answer
    if x == n:
        answer += 1
        return
    for i in range(n):
        col[x] = i
        if check(x):
            BT(x+1)  # 다음 행 체크


n = int(input())
answer = 0

# 한 행에 반드시 하나를 선택할 수 있어야 n개를 선택할 수 있다.
col = [0]*n
BT(0)

print(answer)
