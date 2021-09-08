'''
DP
https://www.acmicpc.net/problem/16287
PyPy3로 채점해야 통과
pypy는 저스트인타임을 이용해서 많이 쓰이는 파이썬의 코드를 캐시화한다음 끌어다 씁니다. 
따라서 반복문의 속도가 수십배정도 개선되는 효과를 가집니다.
'''
import sys
input = sys.stdin.readline
# 무게, 물건 개수
w, n = map(int, input().split())

goods = list(map(int, input().split()))

# 물건 2개의 합 가능 여부를 저장할 dp
dp = [0]*400001  # 물건 하나의 최대 무게 : 200000
out = False
a = "NO"

for i in range(n):
    for j in range(i+1, n):
        t = goods[i]+goods[j]
        if t > w or w-t > 400000:
            continue
        if dp[w-t]:
            out = True
            a = "YES"
            break
    if out:
        break
    for k in range(i):
        t = goods[i] + goods[k]
        if t < w:
            dp[t] = 1

print(a)
