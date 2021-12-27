"""
https://www.acmicpc.net/problem/1068
"""
import sys
'''
트리의 정의 : 사이클이 없는 그래프
즉 방향성이 있는 그래프처럼 생각하면 된다. 
부모 노드는 다음 경로로 자식 노드를 기억해둔다고 생각하자.
리프 노드는 다음 경로가 없는 노드가 된다. 즉 graph[node] = []인 node가 리프노드이다.
'''


def dfs():
    global count
    if len(stack) == 0:
        return
    now = stack.pop()
    if len(graph[now]) == 0:
        count += 1
        return
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs()


input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
delete = int(input())
graph = [[] for _ in range(n)]
visited = [False]*n
stack = []
for i in range(n):
    if i == delete:
        continue
    if tree[i] == -1:
        stack.append(i)
        visited[i] = True
    else:
        graph[tree[i]].append(i)

count = 0
dfs()
print(count)
