"""
https://www.acmicpc.net/problem/1374
"""
import sys
import heapq
input = sys.stdin.readline

# 강의의 개수  100000 이하
n = int(input())
h = []
full = []

for _ in range(n):
    # 강의 번호, 강의 시작 시간, 강의 종료 시간 (0 이상 10억 이하)
    num, start, end = map(int, input().split())
    heapq.heappush(h, (start, end))

heapq.heappush(full, heapq.heappop(h)[1])
ans = 1
while h:
    if len(full) == 0:  # 지금 강의중인 강의실이 없다면
        heapq.heappush(full, heapq.heappop(h)[1])
        continue  # 남은 수업 개수가 없을 수도 있으니 넘김.
    if full[0] > h[0][0]:  # 현재 강의가 가장 빨리 끝나는 시각보다 새로운 강의의 시작시간이 앞선다면
        heapq.heappush(full, heapq.heappop(h)[1])
        # 현재 강의 중인 개수 > 최대 강의실 개수
        if len(full) > ans:
            ans += 1
    else:
        heapq.heappop(full)

print(ans)
