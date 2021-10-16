"""
https://www.acmicpc.net/problem/11000
"""
import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(h, (s, t))

full = []
heapq.heappush(full, heapq.heappop(h)[1])
ans = 1
while h:
    if len(full) == 0:
        heapq.heappush(full, heapq.heappop(h)[1])
        continue
    # s, t = heapq.heappop(h)
    # if s < full[0]:
    #     heapq.heappush(full, t) 이렇게 쓰면 틀렸다고 한다. 왜지? 같은 로직 아닌가?
    # 같은 로직 아니었음!!!! if문에 따라 pop을 할 수도 안 할 수도 있는 거였으니까!!
    if full[0] > h[0][0]:
        heapq.heappush(full, heapq.heappop(h)[1])
        if len(full) > ans:
            ans += 1
    else:
        heapq.heappop(full)

print(ans)
