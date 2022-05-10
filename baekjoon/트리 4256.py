"""
https://www.acmicpc.net/problem/4256
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(1100)
# Python 3 의 기본 재귀 깊이 제한은 1000 이고, Pypy 3 의 기본 재귀 깊이 제한은 1300 이 약간 넘습니다.


def post_order(pre, inorder):
    if len(inorder) <= 1:
        return inorder
    x = pre[0]
    for i in range(len(inorder)):
        if inorder[i] == x:
            return post_order(pre[1:i+1], inorder[:i]) + post_order(pre[i+1:], inorder[i+1:]) + [x]


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    print(*post_order(preorder, inorder))
