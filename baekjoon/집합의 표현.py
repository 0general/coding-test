"""
https://www.acmicpc.net/problem/1717
"""
import sys
sys.setrecursionlimit(10**5)

def find_parent(i):
    if parent[i] != i:
        parent[i] = find_parent(parent[i])
    return parent[i]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# 0 ~ n 까지 n+1개의 집합, 연산 개수 m개
n, m = map(int, sys.stdin.readline().split())
parent = {i:i for i in range(n+1)}

for _ in range(m):
    query, a, b = list(map(int, sys.stdin.readline().split()))
    if query == 0: # union
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
