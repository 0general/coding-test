"""
https://www.acmicpc.net/problem/13334
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]
arr.sort(key=lambda x: x[1])  # 끝 점 기준 정렬
d = int(input())


mx = 0
end = arr[0][1]
h = []
for s, e in arr:
    if e == end:
        if s >= end-d:
            heapq.heappush(h, s)  # 범위에 해당하는 시작점만 담아두면 된다.
    else:
        end = e
        if s >= end - d:
            heapq.heappush(h, s)
        while h and h[0] < end-d:
            heapq.heappop(h)
    mx = max(mx, len(h))

print(mx)
