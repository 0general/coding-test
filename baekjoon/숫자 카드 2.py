"""
https://www.acmicpc.net/problem/10816
"""
import sys

input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()

M = int(input())
nums = list(map(int, input().split()))
check = [0 for _ in range(M)]
dic = dict()


def find_num(num):
    s, e = 0, N-1
    idx = -1
    while s <= e:
        mid = (s+e)//2
        if cards[mid] == num:
            idx = mid
            e = mid - 1
        elif cards[mid] < num:
            s = mid + 1
        else:
            e = mid - 1

    if idx == -1:
        return 0
    s, e = 0, N-1
    temp = -1
    while s <= e:
        mid = (s+e)//2
        if cards[mid] == num:
            temp = mid
            s = mid + 1
        elif cards[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return temp - idx + 1


for i in range(M):
    if nums[i] in dic:
        check[i] = dic[nums[i]]
        continue
    check[i] = find_num(nums[i])
    dic[nums[i]] = check[i]

print(*check)
