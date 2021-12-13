"""
https://www.acmicpc.net/problem/1965
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
nums = list(map(int, input().rstrip().split()))

for num in nums:
    if len(arr) == 0:
        arr.append(num)
    else:
        if arr[-1] < num:
            arr.append(num)
            continue
        if arr[-1] > num:
            s, e = 0, len(arr)-1
            ans = 0
            while s <= e:
                mid = (s+e)//2
                if arr[mid] >= num:
                    ans = mid
                    e = mid - 1
                else:
                    s = mid + 1
            arr[ans] = num

print(len(arr))
