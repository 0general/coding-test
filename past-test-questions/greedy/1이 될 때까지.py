'''
어떠한 수 N이 1이 될 때까지 두 가지 방법 중 하나를 반복적으로 선택하여 수행
1. N에서 1을 뺀다.
2. N이 K로 나누어떨어질 때, N을 K로 나눈다.
N은 2 이상 10만 이하, K는 2 이상 N만 이하 
N은 항상 K 이상
'''

n, k = map(int, input("N과 K를 순서대로 입력하시오 : ").split())
cnt = 0

while n//k >= 0:
    if n//k == 0:
        cnt = cnt + n-1
        break
    else:
        if n % k == 0:
            n = n//k
            cnt += 1
        else:
            while n % k != 0:
                n -= 1
                cnt += 1

print("최소 횟수 : ", cnt)
