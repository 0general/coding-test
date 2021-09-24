'''
https://www.acmicpc.net/problem/1707
'''
import sys
from collections import deque
input = sys.stdin.readline

# 연결되어 있는 간선을 모두 끊을 수 있는가?


def bfs():
    while queue:
        i = queue.popleft()
        for j in arr[i]:
            if visit[j] == -1:
                visit[j] = color[visit[i]]
                queue.append(j)
            else:
                if visit[j] == visit[i]:
                    return False
    return True


ok = True
color = {1: 0, 0: 1}
k = int(input())  # case 수
arr = []  # 간선

for _ in range(k):
    ok = True
    v, e = map(int, input().split())  # 노드 수, 간선 수
    arr = [[] for _ in range(v+1)]
    visit = [-1] * (v+1)  # 방문 확인
    # 인접 리스트
    for _ in range(e):
        u1, u2 = map(int, input().split())
        arr[u1].append(u2)
        arr[u2].append(u1)

    queue = deque()
    for i in range(1, v+1):
        if visit[i] == -1:  # 방문한 적이 없으면
            visit[i] = 0
            queue.append(i)
            ok = bfs()
        if not ok:
            print("NO")
            break
    if ok:
        print("YES")
