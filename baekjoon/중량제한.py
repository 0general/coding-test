"""
https://www.acmicpc.net/problem/1939
"""
# 다양한 풀이가 가능한 문제
# 이분탐색, 다익스트라, 유니온 파인드
import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [dict() for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a][b] = max(arr[a].get(b, 0), arr[b].get(a, 0), c)
    arr[b][a] = arr[a][b]

cap = [-1]*(N+1)
A, B = map(int, input().split())
h = []
heapq.heappush(h, (-(int(1e9)+1, A)))

while h:
    c, n = heapq.heappop(h)
    c = -c
    if cap[n] > c:
        continue
    for i in arr[n]:
        t = min(arr[n][i], c)
        if cap[i] < t:
            cap[i] = t
            heapq.heappush(h, (-t, i))
    '''
    아래의 주석 부분 코드가 들어가면 틀린다. 
    왜냐하면 처음으로 도착한 코드는 지금까지 최대의 중량값을 보장하지만 B까지는 가는데 최대값을 보장하지는 않는다.
    ex. A -3-> C -1-> B vs A -2-> C -2-> B 의 두 가지 경로에 있을 때 C에서 출력을 해버리면 정답은 2지만 1을 출력한다. 
    #     if i == B:
    #         print(cap[i])
    #         break
    # else:
    #     continue
    # break
    '''

print(cap[B])
