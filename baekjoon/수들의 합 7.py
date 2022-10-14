"""
https://www.acmicpc.net/problem/2268
"""
import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0]*N

h = math.ceil(math.log2(N))+1
size = 1 << h
tree = [0]*size


def sum(node, s, e, i, j):
    if i > e or j < s:
        return 0
    if i <= s and e <= j:
        return tree[node]
    return sum(node*2, s, (s+e)//2, i, j) + sum(node*2 + 1, (s+e)//2 + 1, e, i, j)


def modify(node, s, e, i, k):
    if i < s or e < i:
        return
    tree[node] += k
    if s != e:
        modify(node*2, s, (s+e)//2, i, k)
        modify(node*2 + 1, (s+e)//2 + 1, e, i, k)


for _ in range(M):
    o, i, j = map(int, input().split())
    if o == 0:
        i, j = min(i, j), max(i, j)
        print(sum(1, 0, N-1, i-1, j-1))
    else:
        i -= 1
        k = j - arr[i]
        arr[i] = j
        modify(1, 0, N-1, i, k)
