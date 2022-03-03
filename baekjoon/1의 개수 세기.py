"""
https://www.acmicpc.net/problem/9527
"""
# 간단한 수학


def prefix_sum(num):
    if num == 0:
        return 0
    i = 0
    sum = 0
    while num >= (1 << i):  # 각 비트 단위대로 0과 1의 주기에 맞춰 수를 세준다.
        share = (num+1)//(1 << (i+1))
        remainder = (num+1) % (1 << (i+1))
        sum += share*(1 << i)
        if remainder >= (1 << i):
            sum += remainder - (1 << i)
        i += 1
    return sum


A, B = map(int, input().split())

print(prefix_sum(B)-prefix_sum(A-1))
