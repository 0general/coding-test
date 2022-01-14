"""
https://www.acmicpc.net/problem/1005
"""
# 간단하게 메모이제이션 + 재귀 (or DP+DFS)로 푼 문제
# 위상정렬로도 가능하다는데 알아볼것.
import sys


def find_time(idx):
    global parent, dp
    if len(parent[idx]) == 0:
        return dp[idx]
    temp = 0
    while parent[idx]:
        temp = max(temp, find_time(parent[idx].pop()))
    dp[idx] += temp
    return dp[idx]


input = sys.stdin.readline


for _ in range(int(input())):
    n, k = map(int, input().split())
    dp = [0] + list(map(int, input().split()))
    parent = [[] for _ in range(n+1)]
    for _ in range(k):
        p, c = map(int, input().split())
        parent[c].append(p)

    print(find_time(int(input())))
