'''
https://www.acmicpc.net/problem/10972
'''
n = int(input())
f = list(map(int, input().split()))

idx = -1
while idx > -n and f[idx] <= f[idx-1]:  # 뒤에서부터 내림차순을 무시하는 위치를 찾는다.
    idx -= 1
if idx == -n:
    print(-1)
else:  # 1 6 4 2 3 5
    j = -1
    while f[idx-1] >= f[j]:  # f[idx-1] 와 바꿀 숫자는 f[idx-1]보다 크지만 뒤에서 가장 작은 수
        j -= 1
    f[idx-1], f[j] = f[j], f[idx-1]
    ans = f[:idx] + sorted(f[idx:])
    for i in ans:
        print(i, end=' ')
