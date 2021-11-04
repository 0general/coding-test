"""
https://www.acmicpc.net/problem/2343
"""
n, m = map(int, input().split())
nums = list(map(int, input().split()))

l, r = max(nums), 1000000000  # 최소 하나의 동영상은 하나의 블루레이에 들어갈 수 있어야 한다.
ans = 0
while l <= r:
    mid = (l+r)//2
    temp = 0
    group = 0
    for i in range(n):
        if (temp + nums[i]) > mid:  # 블루레이 그룹 수 확인
            temp = 0
            group += 1
        temp += nums[i]
    if group >= m:  # group은 0일 때부터 시작함
        l = mid + 1
    else:
        ans = mid
        r = mid-1
print(ans)
