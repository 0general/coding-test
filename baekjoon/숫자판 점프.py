"""
https://www.acmicpc.net/problem/2210
브루트 포스 + dfs. 숫자판의 크기가 커질 경우에는 어떻게 푸는지 고민해볼 것.
"""
import sys


def dfs(i, j, string):
    global answer
    if len(string) == 6:
        if not visited[int(string)]:
            visited[int(string)] = True
            answer += 1
        return
    else:
        for k in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = i+k[0], j + k[1]
            if 0 <= x < 5 and 0 <= y < 5:
                dfs(x, y, string+graph[x][y])


input = sys.stdin.readline
graph = [list(input().rstrip().split()) for _ in range(5)]

visited = [False for i in range(1000000)]
answer = 0
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(answer)
