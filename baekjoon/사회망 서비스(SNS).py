"""
https://www.acmicpc.net/problem/2533
"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6+10)


class TreeDP():
    def __init__(self, N: int) -> None:
        self.n = N
        self.dp = [0]*(N+1)
        self.visited = [0]*(N+1)
        self.edges = [[] for _ in range(N+1)]

    def set_edge(self):
        for i in range(self.n - 1):
            u, v = map(int, input().split())
            self.edges[u].append(v)
            self.edges[v].append(u)

    def visit(self, node):
        self.visited[node] = 1

    def move(self, node) -> bool:
        self.dp[node] = 0
        eld = False  # 얼리어답터인가
        for i in self.edges[node]:
            if self.visited[i]:
                continue
            self.visited[i] = 1
            eld |= not self.move(i)
            self.dp[node] += self.dp[i]
        self.dp[node] += int(eld)
        return eld


tree = TreeDP(int(input()))
tree.set_edge()
tree.visited[1] = 1
tree.move(1)
print(tree.dp[1])
