'''
https://www.acmicpc.net/problem/1450
'''
#from itertools import combinations
'''
import sys
input = sys.stdin.readline


def bruteforce(sum, goods, id, w):
    if id >= len(goods):
        if w <= c:
            sum.append(w)
        return
    bruteforce(sum, goods, id+1, w)
    bruteforce(sum, goods, id+1, w + goods[id])


# n개의 물건, 넣을 수 있는 최대 c의 무게
n, c = map(int, input().split())
goods = list(map(int, input().split()))
goods.sort()

dp = [0] * (c+1)  # 인덱스 : 무게, 값 : 개수
dp[0] = 1
l, r = 0, n-1
while l < r:
    mid = (l+r)//2
    if goods[mid] <= c:
        l = mid + 1
    else:
        r = mid
goods = goods[:r+1]

ans = len(goods)

for i in range(2, len(goods)+1):
    for check in combinations(goods, i):
        if sum(check) <= c:
            ans += 1

print(ans+1)
메모리 초과

# sum = []
# bruteforce(sum, goods, 0, 0)
# print(len(sum))
이것도 메모리 초과
'''
input = sys.stdin.readline

n, c = map(int, input().split())
weight = list(map(int, input().split()))
aw = weight[:n//2]
bw = weight[n//2:]
asum = []
bsum = []


def bruteforce(warr, sum, l, w):
    if l >= len(warr):
        sum.append(w)
        return
    bruteforce(warr, sum, l+1, w)
    bruteforce(warr, sum, l+1, w+warr[l])


def binarySearch(arr, target, start, end):
    while start < end:
        mid = (start + end)//2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


bruteforce(aw, asum, 0, 0)
bruteforce(bw, bsum, 0, 0)
bsum.sort()

cnt = 0
for i in asum:
    if c-i < 0:
        continue
    # c-i보다 작거나 같은 수의 인덱스 = 가능한 모든 수들의 개수
    cnt += binarySearch(bsum, c-i, 0, len(bsum))
print(cnt)
