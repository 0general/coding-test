"""
https://www.acmicpc.net/problem/2666
"""
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
times = int(input())
arr = [int(input())-1 for _ in range(times)]

# dp[idx][a][b] a,b가 열려있을 때 idx번째 문을 여는 최소 이동 횟수
dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(times)]
# 모든 이동마다 2개씩 가능성이 생기므로 가장 마지막 상태부터 역으로 dp를 채워나가야 함


def dfsdp(idx, door1, door2):
    if idx >= times:
        return 0
    target = arr[idx]
    if dp[idx][door1][door2] < 0:
        dp[idx][door1][door2] = \
            min(abs(target-door1) + dfsdp(idx+1, target, door2),
                abs(target-door2) + dfsdp(idx+1, door1, target))
    return dp[idx][door1][door2]


print(dfsdp(0, a, b))
