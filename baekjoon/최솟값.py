"""
https://www.acmicpc.net/problem/10868
"""
import math
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

h = math.ceil(math.log2(N))+1

tree_size = 1 << h
tree = ['']*tree_size


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2),
                         init(node*2+1, (start+end)//2 + 1, end))
    return tree[node]


def find_min(node, start, end, left, right):
    if left > end or right < start:
        return 1000000001
    if left <= start and end <= right:
        return tree[node]
    return min(find_min(node*2, start, (start+end)//2, left, right),
               find_min(node*2+1, (start+end)//2 + 1, end, left, right))


init(1, 0, N-1)


for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(find_min(1, 0, N-1, a, b))
