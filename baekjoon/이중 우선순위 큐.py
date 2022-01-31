"""
https://www.acmicpc.net/problem/7662
"""
import sys
import heapq

input = sys.stdin.readline


for _ in range(int(input())):
    visit = []
    num = 0
    mx = []
    mn = []
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        b = int(b)
        if a == 'I':
            visit.append(b)
            heapq.heappush(mx, (-b, num))
            heapq.heappush(mn, (b, num))
            num += 1
        else:
            if b == -1:
                while mn:
                    _, x = heapq.heappop(mn)
                    if visit[x] != 'x':
                        visit[x] = 'x'
                        break
            else:
                while mx:
                    _, x = heapq.heappop(mx)
                    if visit[x] != 'x':
                        visit[x] = 'x'
                        break
    ans = []
    while mx:
        _, x = heapq.heappop(mx)
        if visit[x] != 'x':
            ans.append(visit[x])
            break
    while mn:
        _, x = heapq.heappop(mn)
        if visit[x] != 'x':
            ans.append(visit[x])
            break
    if len(ans) < 2:
        print('EMPTY')
    else:
        print(*ans)
