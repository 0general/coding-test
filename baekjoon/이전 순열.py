'''
https://www.acmicpc.net/problem/10973
'''

n = int(input())
f = list(map(int, input().split()))  # 숫자 비교 조심

idx = -1
while idx > -n and f[idx] >= f[idx-1]:
    idx -= 1
if idx == -n:
    print(-1)
else:  # 1 6 4 2 3 5
    j = -1
    while f[idx-1] <= f[j]:  # f[idx-1] 와 바꿀 숫자는 f[idx-1]보다 작지만 뒤에서 가장 큰 수
        j -= 1
    f[idx-1], f[j] = f[j], f[idx-1]
    ans = f[:idx] + sorted(f[idx:], reverse=True)
    for i in ans:
        print(i, end=' ')
