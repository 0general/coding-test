"""
https://www.acmicpc.net/problem/1976
"""
import sys


# 전형적인 union find 유형 문제
# 주어진 여행 경로가 가능하려면 모두 연결되어 있어야 한다. 즉 경로의 도시가 모두 연결되어 있는지를 묻고 있다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(i, N+1):
        if arr[j-1]:  # 연결되어 있으면
            union_parent(parent, i, j)


# 한번 지나갔던 길은 이미 갈 수 있기 때문에 겹치는 도시는 확인 안 해도 됨.
arr = set(map(int, input().split()))

p = find_parent(parent, arr.pop())
for a in arr:
    if find_parent(parent, a) != p:
        print("NO")
        break
else:
    print("YES")
