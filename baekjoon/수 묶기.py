"""
https://www.acmicpc.net/problem/1744
"""
import sys

input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
if N < 2:
    print(arr[0])
else:
    i = N-1
    answer = 0
    while i >= 1 and arr[i] > 0:  # 양수 부분 처리
        if arr[i]*arr[i-1] > arr[i]+arr[i-1]:
            answer += arr[i]*arr[i-1]
            i -= 2
            arr.pop()
            arr.pop()
        else:  # 만약 arr[i+1] <= 0이면 자동으로 else문에 해당 양수만 더하게 된다.
            answer += arr[i]
            i -= 1
            arr.pop()
    i = 0
    while i <= len(arr)-1:  # 0을 포함한 음수는 따로 관리
        if i == len(arr)-1:
            answer += arr[i]
            break
        answer += arr[i]*arr[i+1]
        i += 2
    print(answer)
