"""
https://www.acmicpc.net/problem/1088
호석님 무작위 코테 방송 보고 배움
"""
import sys

input = sys.stdin.readline

n = int(input())
original = list(map(int, input().split()))
cake = [i for i in original]
num = [1]*n  # i번째 케이크 나뉜 조각 수
m = int(input())

ans = max(original) - min(original)

for _ in range(m):
    sz, idx = cake[0], 0
    for i in range(1, n):
        if sz < cake[i]:
            sz, idx = cake[i], i

    num[idx] += 1  # idx 케이크가 가장 크다고 선정된 횟수
    # 그 횟수만큼 공평하게 나눠야 조각의 크기 차이를 잘 줄일 수 있음!
    cake[idx] = (original[idx]/num[idx])

    ans = min(ans, max(cake)-min(cake))

print('%.10f' % (ans))
