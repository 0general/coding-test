"""
https://www.acmicpc.net/problem/1043
"""
# 서로소 집합
# 유니온 파인드
import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N+1)]

truth = list(map(int, input().split()))
arr = []

for _ in range(M):
    ls = list(map(int, input().split()))
    arr.append(ls)
    for i in range(1, len(ls)):
        union_parent(parent, ls[1], ls[i])

if truth[0] == 0:
    print(M)
else:
    for i in range(1, len(truth)):
        union_parent(parent, truth[1], truth[i])

    for i in range(M):
        if find_parent(parent, arr[i][1]) == find_parent(parent, truth[1]):
            M -= 1
    print(M)
