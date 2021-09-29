"""
https://www.acmicpc.net/problem/13913
"""
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    sys.exit()

map = [0]*100001
prev = [0]*100001

queue = deque()

cnt = 0
map[n] = cnt
prev[n] = -1
queue.append(n)  # 인덱스
ans = []

while queue:
    now = queue.popleft()
    cnt = map[now]
    for next in (now-1, now+1, 2*now):  # 다음 인덱스
        if 0 <= next < 100001 and map[next] == 0 and next != n:
            map[next] = cnt+1
            prev[next] = now
            queue.append(next)
        if next == k:
            ans.append(str(k))
            s = prev[k]
            while s != -1:
                ans.append(str(s))
                s = prev[s]
            ans.reverse()
            print(" ".join(ans))
            sys.exit()
