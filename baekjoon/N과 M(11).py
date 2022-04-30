"""
https://www.acmicpc.net/problem/15665
"""
import sys

input = sys.stdin.readline

#중복순열
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans_list = set()

def dfs(num,string):
    if num == m:
        if string not in ans_list:
            ans_list.add(string)
            print(string)
        return
    for k in range(n):
        dfs(num+1,string+str(arr[k])+" ")

dfs(0,"")