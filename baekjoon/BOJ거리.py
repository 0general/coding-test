"""
https://www.acmicpc.net/problem/12026
"""
import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = list(input().rstrip())
dic = {'B': 'O', 'O': 'J', 'J': 'B'}
d = ['' for _ in range(n)]
d[0] = 0
h = []
ans = -1
heapq.heappush(h, (0, 0))
while h:
    cost, now = heapq.heappop(h)
    if cost > d[now]:
        continue
    if now == n-1:
        ans = cost
        break
    for i in range(now+1, n):
        if arr[i] == dic[arr[now]]:
            nc = cost+(i-now)**2
            if d[i] == '' or nc < d[i]:
                d[i] = nc
                heapq.heappush(h, (nc, i))

print(ans)
