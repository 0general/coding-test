'''
https://www.acmicpc.net/problem/13023
'''
import sys
# 사람 수, 관계 수
n, m = map(int, input().split())

rel = [[] for _ in range(n)]
visit = [0] * n  # 방문 체크
stack = []


def dfs(i, top):
    stack.append(i)
    top += 1
    visit[i] = 1
    if top >= 4:
        print(1)
        sys.exit()
    for v in rel[i]:
        if not visit[v]:
            dfs(v, top)
    visit[stack[top]] = 0
    stack.pop()
    top -= 1


# 관계 입력
for k in range(m):
    i, j = map(int, input().split())
    rel[i].append(j)
    rel[j].append(i)

for i in range(n):
    stack = []
    top = -1
    if not visit[i]:
        dfs(i, top)
    if top >= 4:
        break

# top이 4 이상일 때 빠져나오지 못 함
print(0)
