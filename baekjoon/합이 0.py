"""
https://www.acmicpc.net/problem/3151
pypy3 27%에서 시간초과 
"""
import sys


def binary_search(s, e, hap):
    global answer
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < -hap:
            s = mid + 1
        elif arr[mid] > -hap:
            e = mid - 1
        else:
            # print(f"i = {i}, j = {j}, mid={mid}, num[-hap] = {num[-hap]}")
            if j < num[-hap][0]:
                answer += num[-hap][1] - num[-hap][0] + 1
            else:
                answer += num[-hap][1]-j
            # print(f"answer = {answer}")
            return


input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
num = [[0, 0] for _ in range(20001)]  # 20001

for i in range(1, N):
    if arr[i] == arr[i-1]:
        num[arr[i]][1] = i
    else:
        num[arr[i]][0] = i
        num[arr[i-1]][1] = i-1
    if i == N-1:
        num[arr[i]][1] = i

answer = 0

for i in range(N-1):
    for j in range(i+1, N):
        hap = arr[i]+arr[j]
        s, e = j+1, N-1
        binary_search(s, e, hap)

print(answer)
