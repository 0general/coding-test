"""
https://www.acmicpc.net/problem/11060
"""
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().rstrip().split()))
dp = [0]*n  # 이 칸에 도달할 수 있는 최소 점프 수
q = deque()

q.append((0))  # 현재 위치

if n == 1:
    print(0)
else:
    while q:
        now = q.popleft()
        for i in range(1, A[now]+1):
            next = now+i
            if next < n and dp[next] == 0:  # 아직 방문 하지 않음.
                dp[next] = dp[now]+1
                q.append((next))
    if dp[n-1] == 0:
        print(-1)
    else:
        print(dp[n-1])
