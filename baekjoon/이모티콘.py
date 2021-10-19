"""
https://www.acmicpc.net/problem/14226
"""
from collections import deque


def bfs():
    while q:
        ns, nm, nc = q.popleft()  # 현재 초, 현재 화면, 클립보드
        if dp[nm] == 0:
            dp[nm] = ns
        if nm == s:
            return
        if nc != 0 and nm + nc < len(dp) and not dp[nm+nc]:  # 붙여넣기
            q.append((ns + 1, nm + nc, nc))
        if nm - 1 > 0 and not dp[nm-1]:
            q.append((ns + 1, nm - 1, nc))  # 이모티콘 지우기
        if nm != nc:
            q.append((ns + 1, nm, nm))  # 클립보드 복사


s = int(input())
clip = 0
monitor = 1
q = deque()
dp = [0]*(2000)  # dp definition : 이모티콘 i개를 만드는데 걸리는 시간
q.append((0, monitor, clip))
bfs()

print(dp[s])
