"""
https://www.acmicpc.net/problem/15663
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = set()
visited = [False]*n

def dfs(num,string):
    if num == m:
        if string not in ans:
            ans.add(string)
            print(string)
        return
    for k in range(n):
        if not visited[k]:
            visited[k] = True
            dfs(num+1,string+str(arr[k])+" ")
            visited[k] = False

dfs(0,"")