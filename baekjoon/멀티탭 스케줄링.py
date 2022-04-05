"""
https://www.acmicpc.net/problem/1700
"""
import sys
from collections import deque

# 앞으로 가장 오랫동안 사용되지 않을 플러그를 뽑는다.
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
visited = [0]*(k+1)
use_time = [deque() for _ in range(k+1)]
for i in range(k):
    use_time[arr[i]].append(i)

for i, num in enumerate(arr):
    if visited[num]:
        use_time[num].popleft()
    else:
        if sum(visited) == n:
            mx = -1
            x = 0
            for i in range(1, k+1):
                if visited[i]:
                    if len(use_time[i]) == 0:
                        x = i
                        break
                    elif use_time[i][0] > mx:
                        mx = use_time[i][0]
                        x = i
            visited[x] = 0
            ans += 1
        use_time[num].popleft()
        visited[num] = 1


print(ans)
