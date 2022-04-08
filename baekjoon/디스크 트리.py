"""
https://www.acmicpc.net/problem/7432
"""
import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(x, path, t):
    global next
    print(' '*t+x)
    for s in sorted(next[path]):
        dfs(s, path+'.'+s, t+1)


n = int(input())
q = set()
next = defaultdict(set)

for _ in range(n):
    dir = input().rstrip().split('\\')
    for i in range(len(dir)):
        if i == 0:
            q.add(dir[i])
            continue
        # 디렉토리 경로를 전부 저장해야한다. 다른 겅로에 동일 이름의 파일이 존재 가능
        next['.'.join(dir[:i])].add(dir[i])


for now in sorted(q):
    dfs(now, now, 0)
