"""
https://www.acmicpc.net/problem/1991
"""
import sys


def preorder(idx):
    print(chr(idx+65), end='')
    if child[idx][0] != '.':
        preorder(ord(child[idx][0])-65)
    if child[idx][1] != '.':
        preorder(ord(child[idx][1])-65)


def inorder(idx):
    if child[idx][0] != '.':
        inorder(ord(child[idx][0])-65)
    print(chr(idx+65), end='')
    if child[idx][1] != '.':
        inorder(ord(child[idx][1])-65)


def postorder(idx):
    if child[idx][0] != '.':
        postorder(ord(child[idx][0])-65)
    if child[idx][1] != '.':
        postorder(ord(child[idx][1])-65)
    print(chr(idx+65), end='')


input = sys.stdin.readline
child = [['.', '.'] for _ in range(26)]  # 왼쪽 자식, 오른쪽 자식 저장  A:0~Z:25

n = int(input())
for _ in range(n):
    p, lc, rc = input().rstrip().split()
    child[ord(p)-65] = [lc, rc]

preorder(0)
print()
inorder(0)
print()
postorder(0)
