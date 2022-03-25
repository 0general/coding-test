"""
https://www.acmicpc.net/problem/2887
"""
import sys

input = sys.stdin.readline


def find_parent(r):
    if parent[r] == r:
        return parent[r]
    parent[r] = find_parent(parent[r])
    return parent[r]


n = int(input())
parent = [i for i in range(n)]
loc = []
for i in range(n):
    x, y, z = map(int, input().split())
    loc.append([x, y, z, i])

edge = []
for j in range(3):
    loc.sort(key=lambda x: x[j])  # 각 축 상에서 일직선으로 정렬
    for i in range(1, n):
        # 일직선이므로 앞 뒤 한 좌표씩만 확인하면 됨.
        edge.append((abs(loc[i][j]-loc[i-1][j]), loc[i][3], loc[i-1][3]))

edge.sort(key=lambda x: x[0])  # 최소 간선으로 sort

answer = 0
num = 0
for dist, i, j in edge:
    i = find_parent(i)
    j = find_parent(j)
    if i != j:  # union
        parent[i] = j
        num += 1
        answer += dist
    if num == n-1:  # 최소 신장 트리 = 스패닝 트리는 최소 가중치를 보장하는 사이클이 없는 최소 간선의 개수를 가진다.
        break

print(answer)
