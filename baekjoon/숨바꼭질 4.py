"""
https://www.acmicpc.net/problem/13913
"""
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

map = [0]*100001
prev = [0]*100001

queue = deque()
ans = []

cnt = 0
map[n] = cnt
prev[n] = -1
queue.append(n)  # 인덱스

while queue:
    now = queue.popleft()
    if now == k:
        print(map[now])
        ans.append(str(now))
        s = prev[now]
        while s != -1:
            ans.append(str(s))
            s = prev[s]
        ans.reverse()
        print(" ".join(ans))
        break

    for next in (now-1, now+1, 2*now):  # 다음 인덱스
        if 0 <= next < 100001 and map[next] == 0 and next != n:
            map[next] = map[now]+1
            prev[next] = now
            queue.append(next)
