"""
https://www.acmicpc.net/problem/1202
"""
import sys
import heapq

input = sys.stdin.readline

# 보석 개수, 가방 개수
N, K = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: x[0])  # 무게 정렬
bags.sort()

h = []

ans = 0
i = 0
for bag in bags:
    # 현재 가방 수용 가능 무게보다 작은 보석의 가치를 모두 heap에 삽입
    while i < N and jewels[i][0] <= bag:
        heapq.heappush(h, -jewels[i][1])
        i += 1

    if h:
        ans -= heapq.heappop(h)

print(ans)
