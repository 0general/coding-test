"""
https://www.acmicpc.net/problem/1699
"""
from math import sqrt
from collections import deque


def solution2(n):  # using queue
    ls = []
    q = deque()
    dp = [0]*(n+1)
    for i in range(1, int(sqrt(n))+1):
        a = i**2
        ls.append(a)
        q.append(a)
        dp[a] = 1

    while q:
        now = q.popleft()
        for i in ls:
            next = now + i
            if next > n:
                break
            if not dp[next]:
                dp[next] = dp[now]+1
                q.append(next)
    print(dp[n])


def solution(n):
    x = int(sqrt(n))

    # 구해야 하는 값 : n의 제곱수 항 최소 개수
    dp = [0]*(n+1)
    for i in range(1, x+1):
        dp[i**2] = 1  # 초깃값들. 제곱수들을 항이 1개

    for i in range(2, n+1):
        if dp[i] == 0:  # 아직 구하지 않은 수라면
            a = int(sqrt(i))
            # 무작정 이걸로 끝내버린다면 12 = 3^2 + (1^2)*3 으로 4가 되어버림. 실제 답은 (4^2)*3으로 3
            dp[i] = dp[i-a**2] + 1
            for k in range(1, a):
                if dp[i] == 1 or dp[i] == 2:
                    break
                dp[i] = min(dp[i], dp[i-k**2]+1)
    print(dp[n])


solution2(int(input()))
