"""
https://www.acmicpc.net/problem/2644
"""
import sys
from collections import deque


input = sys.stdin.readline
n = int(input())  # 사람 수
me, find = map(int, input().split())

p = [[-1, []] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(int(input())):
    i, j = map(int, input().split())
    p[j][0] = i  # j의 부모는 i
    p[i][1].append(j)  # i의 자식은 j

    '''
    부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
    이 조건 제대로 안 읽고 내 맘대로 더 작은 수가 조상이라고 넣었다가 한번 틀렸었음.
    '''

ans = -1
q = deque()
visited[me] = True
q.append((me, 0))
while q:
    now, line = q.popleft()
    if now == find:
        ans = line
        break
    for c in p[now][1]:  # 내 자식들
        if not visited[c]:
            visited[c] = True
            q.append((c, line+1))
    if p[now][0] != -1 and not visited[p[now][0]]:
        visited[p[now][0]] = True
        q.append((p[now][0], line+1))

print(ans)
