"""
https://www.acmicpc.net/problem/2263
"""
import sys

input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

num = len(inorder)
preorder = [0] * num
