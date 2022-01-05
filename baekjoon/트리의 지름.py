"""
https://www.acmicpc.net/problem/1967
"""
import sys

sys.setrecursionlimit(int(1e5))


def dfs(node, dist):
    for idx, d in arr[node]:
        cost = dist+d
        if distance[idx] == -1:  # 갱신된 적이 없는 노드 visited 역할
            distance[idx] = cost
            dfs(idx, cost)


input = sys.stdin.readline
n = int(input())

distance = [-1]*(n+1)
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))


# 어떤 점이든 가장 먼 점이 지름를 이루는 양 끝 점 중 한 점이다.
# 참고 : https://blog.myungwoo.kr/112

distance[1] = 0
dfs(1, 0)
dia = distance.index(max(distance))

distance = [-1]*(n+1)
distance[dia] = 0
dfs(dia, 0)
print(max(distance))
