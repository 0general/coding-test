"""
https://www.acmicpc.net/problem/16928
"""
import sys
from collections import deque

input = sys.stdin.readline

graph = [0]*(101)
q = deque()
# 사다리의 수 n, 뱀의 수 m
n, m = map(int, input().split())

for _ in range(n+m):  # 어차피 사다리나 뱀이나 현재 위치를 이동시키는 것이다.
    fm, to = map(int, input().split())
    graph[fm] = to

# graph의 숫자가 0이면 아직 도달하지 않는 거고 1이면 이미 방문한 곳이다.
# 1번 칸과 100번 칸은 뱀이나 사다리의 시작 또는 끝이 아니라고 했으므로 graph[1] = 0, graph[100] = 0
graph[1] = 1  # 방문 처리
# q 안에는 주사위를 돌릴 칸만이 들어가게 됨.
q.append((1, 0))

while q:
    now, cnt = q.popleft()  # 주사위를 돌릴 현재 위치
    for i in range(1, 7):  # 1부터 6까지
        next = now + i  # 다음 방문 위치
        if next <= 100 and graph[next] != 1:  # 방문한 적이 없을 때
            while graph[next] > 1:  # 이 위치에 방문한 적이 없고, 뱀이나 사다리가 있다면
                temp = graph[next]  # 그 다음으로 이동하는 곳
                graph[next] = 1  # 방문처리
                next = temp
            # 주사위를 돌릴 수 있는 위치
            if next == 100:
                print(cnt+1)
                sys.exit()
            if graph[next] == 0:
                graph[next] = 1
                q.append((next, cnt+1))
