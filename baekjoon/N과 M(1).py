'''
https://www.acmicpc.net/problem/15649
'''
# from itertools import permutations
#
# n, m = map(int, input().split())
# arr = list(permutations(range(1, n+1), m))
#
# for i in arr:
#     for j in i:
#         print(j, end=' ')
#     print()
#

# itertools 없이 순열구하기
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
visited = [False]*n
def dfs(num,string):
    if num == m:
        print(string)
        return
    for idx, k in enumerate(arr):
        if not visited[idx]:
            visited[idx] = True
            dfs(num+1,string+str(k)+" ")
            visited[idx] = False

dfs(0,"")