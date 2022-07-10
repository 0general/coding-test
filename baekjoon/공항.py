"""
https://www.acmicpc.net/problem/10775
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100010)
G = int(input())
P = int(input())


def union(a, b, maxairport):
    a = find(a, maxairport)
    b = find(b, maxairport)
    if a < b:
        maxairport[b] = a
    else:
        maxairport[a] = b


def find(a, maxairport):
    if maxairport[a] == a:
        return a
    maxairport[a] = find(maxairport[a], maxairport)
    return maxairport[a]


maxairport = [i for i in range(G+1)]  # gi게이트를 입력받은 비행기가 갈 수 있는 최대 게이트
ans = 0
flag = False
for i in range(P):
    a = int(input())
    if flag:
        continue
    a = find(a, maxairport)
    if a == 0:
        flag = True
    else:
        union(a, a-1, maxairport)
        ans += 1
print(ans)
