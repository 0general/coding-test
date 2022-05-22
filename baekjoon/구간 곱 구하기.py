"""
https://www.acmicpc.net/problem/11505
init 할 때도 모듈러 연산을 해줘야한다. 그렇지 않으면 처음부터 큰 값이 들어가있어서 시간초과가 발생한다.
나머지 연산 딱 하나 추가해줬는데 시간초과를 벗어남
"""
import math
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
h = math.ceil(math.log2(N))+1
size = 1 << h

Tree = ['']*size
MOD = 1000000007


def init(node, start, end):
    if start == end:
        Tree[node] = arr[start]
    else:
        Tree[node] = init(node*2, start, (start+end)//2) * \
            init(node*2+1, (start+end)//2 + 1, end) % MOD
    return Tree[node]


def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return Tree[node]
    if start == end:
        if start == idx:
            Tree[node] = diff
        return Tree[node]
    Tree[node] = (update(node*2, start, (start+end)//2, idx, diff) *
                  update(node*2+1, (start+end)//2+1, end, idx, diff)) % MOD
    return Tree[node]


def multiply(node, start, end, left, right):
    if end < left or start > right:
        return 1
    if left <= start and end <= right:
        return Tree[node]
    return (multiply(node*2, start, (start+end)//2, left, right)*multiply(node*2+1, (start+end)//2+1, end, left, right)) % MOD


init(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(multiply(1, 0, N-1, b-1, c-1))
