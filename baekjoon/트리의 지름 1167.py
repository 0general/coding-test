"""
https://www.acmicpc.net/problem/1167
"""
import sys

sys.setrecursionlimit(100005)


def dfs(node, dist):
    for n, c in arr[node]:
        if distance[n] == -1:
            distance[n] = dist + c
            dfs(n, distance[n])


input = sys.stdin.readline

v = int(input())

distance = [-1]*(v+1)

arr = [[] for _ in range(v+1)]

for _ in range(v):
    temp = list(map(int, input().split()))
    s = temp[0]
    i = 1
    while temp[i] != -1:
        arr[s].append((temp[i], temp[i+1]))
        arr[temp[i]].append((s, temp[i+1]))
        i += 2

distance[1] = 0
dfs(1, 0)

dia = distance.index(max(distance))

distance = [-1]*(v+1)
distance[dia] = 0
dfs(dia, 0)

print(max(distance))
