"""
https://www.acmicpc.net/problem/16198
"""
import sys


def BT(hap, cnt):
    global mx
    if cnt == n-2:
        mx = max(mx, hap)
    for i in range(1, n-1):
        if not visited[i]:
            visited[i] = True
            a = 0
            for d in range(i-1, -1, -1):
                if not visited[d]:
                    a = w[d]
                    break
            for u in range(i+1, n):
                if not visited[u]:
                    a *= w[u]
                    break
            BT(hap + a, cnt + 1)
            visited[i] = False


input = sys.stdin.readline

n = int(input())
w = list(map(int, input().split()))
visited = [False]*(n)
mx = 0
BT(0, 0)
print(mx)
