'''
https://www.acmicpc.net/problem/15650
'''
# from itertools import combinations
#
# n, m = map(int, input().split())
# arr = list(combinations(range(1, n+1), m))
#
# for i in arr:
#     for j in i:
#         print(j, end=' ')
#     print()

# itertools 없이 조합 짜기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]

def dfs(i,num,string):
    if num == m:
        print(string)
        return
    if i >= n or n-i < m-num:
        return
    dfs(i+1,num+1,string+str(arr[i])+" ")
    dfs(i+1,num,string)

dfs(0,0,"")