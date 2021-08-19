'''
https://www.acmicpc.net/problem/2437

'''
'''
#시간 초과

# 저울 추의 개수 N
n = int(input())
ls = list(map(int, input().split()))
ls.sort()
ans = ls[-1] + 1
for i in range(1, ls[-1]):
    if i not in ls:
        s = i
        for j in list(reversed(ls)):
            if j > s:
                continue
            else:
                s -= j
            if s == 0:
                break
        if s != 0:
            ans = i
            break
    else:
        continue

print(ans)
'''
n = int(input())
ls = list(map(int, input().split()))
ls.sort()
target = 1
for i in ls:
    if target < i:
        break
    target += i

print(target)
