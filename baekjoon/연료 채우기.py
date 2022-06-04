"""
https://www.acmicpc.net/problem/1826
"""
import sys
import heapq

input = sys.stdin.readline

N = int(input())
num = 0
rest = [list(map(int, input().split())) for _ in range(N)]
rest.sort(key=lambda x: (x[0], -x[1]))
h = []
dest, now = map(int, input().split())


i = 0
while i < N:
    if now >= rest[i][0]:
        heapq.heappush(h, -rest[i][1])
        i += 1
    else:
        while h and now < rest[i][0]:
            now -= heapq.heappop(h)
            num += 1
        if len(h) == 0 and now < rest[i][0]: # 이거 처리 안 해줬다가 무한 루프 걸림
            break

while h and now < dest:
    now -= heapq.heappop(h)
    num += 1

if now < dest:
    print(-1)
else:
    print(num)
