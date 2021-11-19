"""
https://www.acmicpc.net/problem/12852
"""
from collections import deque

n = int(input())
q = deque()

dp = [0]*(n+1)
cnt = 0
q.append((n, cnt))
while q:
    now, c = q.popleft()
    if now == 1:
        print(c)
        break
    if now % 3 == 0 and dp[now//3] == 0:
        a = now//3
        dp[a] = now  # 이전 값 저장
        q.append((a, c+1))
    if now % 2 == 0 and dp[now//2] == 0:
        a = now//2
        dp[a] = now
        q.append((a, c+1))
    if now-1 > 0 and dp[now-1] == 0:
        a = now-1
        dp[a] = now
        q.append((a, c+1))

ans = [1]
while dp[ans[-1]] != 0:
    ans.append(dp[ans[-1]])

ans.reverse()
print(*ans)
