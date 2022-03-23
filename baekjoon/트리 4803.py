"""
https://www.acmicpc.net/problem/4803
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(510)


def find_parent(i):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent[i])
    return parent[i]


def union_parent(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


case = 0
while True:
    case += 1
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n+1)]
    cycle = [False]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        a = find_parent(a)
        b = find_parent(b)
        if a != b:
            union_parent(a, b)
            if cycle[a] or cycle[b]:
                cycle[a] = True
                cycle[b] = True
        else:
            cycle[a] = True
            cycle[b] = True
    t = 0
    for i in range(1, n+1):
        if i == find_parent(i) and not cycle[i]:
            t += 1
    if t == 0:
        print(f"Case {case}: No trees.") # 사이클을 제외한 트리의 개수를 세기
    elif t == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: A forest of {t} trees.")
