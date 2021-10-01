"""
https://www.acmicpc.net/problem/7578
"""
import sys
import math


def update(node, start, end, idx):  # 갱신할 노드 범위
    if idx < start or end < idx:  # 범위를 벗어나는 경우
        return 0

    if start == end:
        tree[node] = 1
        return tree[node]

    mid = (start + end)//2
    update(node*2, start, mid, idx)
    update(node*2+1, mid+1, end, idx)
    tree[node] = tree[2*node]+tree[node*2+1]
    return tree[node]

# 찾아갈 범위에 해당하는 구간합 값을 반환


def query(node, start, end, left, right):  # tree node, tree node 범위, 찾아갈 범위
    if right < start or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2 + 1, mid+1, end, left, right)


input = sys.stdin.readline
n = int(input())
A = input().split()

B = dict()
idx = 0
for num in input().split():
    B[num] = idx
    idx += 1

h = int(math.ceil(math.log2(n)))
size = 2 ** (h+1)

tree = [0] * size

answer = 0
for num in A:
    now = B[num]  # 줄을 연결했을 때 B의 위치 인덱스
    # 노드는 1부터 시작
    answer += query(1, 0, n-1, now, n-1)  # 하나의 선이 그어질 때 찾아가며 만나는 선들의 합

    update(1, 0, n-1, now)  # 트리 갱신


print(answer)
