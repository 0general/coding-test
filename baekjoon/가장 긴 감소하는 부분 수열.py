"""
https://www.acmicpc.net/problem/11722
동일 코드 시간 차이
29200  KB	68	ms Python 3 
125284 KB	112	ms PyPy3
"""
import sys


def BT(num):  # 내림차순 Binary Search
    if len(stack) == 0:
        stack.append(num)
        return
    start, end = 0, len(stack)-1
    ans = len(stack)
    while start <= end:  # num의 위치 찾기
        mid = (start+end)//2
        if stack[mid] <= num:  # num이 크거나 같으면 더 앞쪽으로 가야 함
            ans = mid
            end = mid-1
        else:  # num이 더 작으면 뒤쪽 그룹에서 찾기
            start = mid + 1
    if ans == len(stack):
        stack.append(num)
    else:
        stack[ans] = num
    return


input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
stack = []
for num in seq:
    BT(num)

print(len(stack))
