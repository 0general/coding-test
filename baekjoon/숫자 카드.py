'''
https://www.acmicpc.net/problem/10815
'''
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
card.sort()

m = int(input())
check_list = list(map(int, input().split()))

for item in check_list:
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if card[mid] < item:
            l = mid+1
        elif card[mid] == item:
            print(1, end=" ")
            break
        else:
            r = mid-1
    if l > r:
        print(0, end=" ")
