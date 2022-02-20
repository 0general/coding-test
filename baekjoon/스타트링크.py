"""
https://www.acmicpc.net/problem/5014
"""
import sys
from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False]*(1000001)

q = deque()
visited[S] = True
q.append((S, 0))
ans = -1
if S == G:
    print(0)
else:
    while q:
        now, t = q.popleft()
        for i in (U, -D):
            temp = now + i
            if temp > 0 and temp <= F and not visited[temp]:
                visited[temp] = True
                if temp == G:
                    ans = t+1
                    break
                q.append((temp, t+1))
        else:
            continue
        break
    if ans == -1:
        print("use the stairs")
    else:
        print(ans)
