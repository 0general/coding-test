"""
https://www.acmicpc.net/problem/2042
"""
import math
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

h = math.ceil(math.log2(N))+1
tree_size = 1 << (h+1)
tree = ['']*tree_size

arr = [int(input()) for _ in range(N)]


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + \
            init(node*2+1, (start+end)//2+1, end)
    return tree[node]


def update(node, start, end, idx, diff):
    if idx < start or end < idx:
        return
    tree[node] += diff
    if start != end:
        update(node*2, start, (start+end)//2, idx, diff)
        update(node*2+1, (start+end)//2+1, end, idx, diff)


def sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sum(node*2, start, (start+end)//2, left, right)+sum(node*2+1, (start+end)//2+1, end, left, right)


init(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        diff = c-arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    else:
        c -= 1
        print(sum(1, 0, N-1, b, c))
