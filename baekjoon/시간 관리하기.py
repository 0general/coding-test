'''
https://www.acmicpc.net/problem/6068
'''
import sys
import heapq

input = sys.stdin.readline
N = int(input())
h = []
for i in range(N):
    t, e = map(int, input().split())
    heapq.heappush(h, (-e, t))

now = -h[0][0]
while h:
    e, t = heapq.heappop(h)
    e = -e
    if e >= now:  # 이번 일이 끝내야 할 시각이 현재 시각보다 여유가 있다면
        now -= t
    else:  # 현재 시각보다 이전에 끝내야만 한다면
        now = e-t
    if now < 0:
        now = -1
        break

print(now)
