"""
https://www.acmicpc.net/problem/1525
"""
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

arr = []
for _ in range(3):
    arr.extend(list(map(int, input().split())))

id = arr.index(0)
visited = defaultdict(bool)
visited[tuple(arr)] = True

q = deque()
q.append((arr, 0, id))
ans = -1
while q:
    now, num, idx = q.popleft()
    if now == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        ans = num
        break
    for i in [3, -3, 1, -1]:
        next = idx+i
        if next < 0 or next >= 9:
            continue
        if (idx % 3 == 2 and i == 1) or (idx % 3 == 0 and i == -1):  # 여기 반드시 주의
            continue
        temp = [k for k in now]
        temp[next], temp[idx] = temp[idx], temp[next]
        if visited[tuple(temp)]:
            continue
        visited[tuple(temp)] = True
        q.append((temp, num+1, next))

print(ans)
