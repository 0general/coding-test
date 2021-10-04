"""
https://www.acmicpc.net/problem/10971
"""


def backtracking(a, temp, cnt):
    global cost
    if cnt == n-1:
        if w[a][i] != 0:
            cost = min(cost, temp + w[a][i])
            return
    for j, jcost in enumerate(w[a]):
        if jcost != 0 and not visit[j]:
            visit[j] = True
            backtracking(j, temp+jcost, cnt+1)
            visit[j] = False


# 도시 수 n은 1보다 크고 10보다 작거나 같은 수
n = int(input())
w = []

for _ in range(n):
    w.append(list(map(int, input().split())))

cost = int(1e9)

for i in range(n):  # 시작 노드
    visit = [False] * n
    temp = 0  # 가격 표시
    cnt = 0
    visit[i] = True
    backtracking(i, temp, cnt)

print(cost)
