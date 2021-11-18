"""
https://www.acmicpc.net/problem/1966
"""
from collections import deque
import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    # 문서 개수 , 궁금한 문서 인덱스
    n, m = map(int, input().split())
    # n개 문서
    docs = list(map(int, input().rstrip().split()))
    q = deque([i for i in range(n)])
    h = []
    cnt = 0
    for d in docs:
        heapq.heappush(h, -d)
    while q:
        now = q.popleft()  # index
        if docs[now] == -h[0]:  # 가장 중요도가 높은 문서인지
            cnt += 1
            heapq.heappop(h)
            if now == m:
                break
        else:
            q.append(now)
    print(cnt)
