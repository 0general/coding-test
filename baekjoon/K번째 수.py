"""
https://www.acmicpc.net/problem/1300
"""
# 배열의 크기 n*n 1부터 시작
n = int(input())
# 찾으려는 인덱스 1부터 시작
k = int(input())

# 행렬의 i행 (1*i ~ n*i)에 어떤 수 x보다 작거나 같은 수의 개수 = 시그마 x//i (if x//i > n, n)
# 위에서 구한 값이 k이면 종료
answer = 0
start, end = 1, k  # 찾으려는 값의 범위 1*1 ~ n*n까지 가능한데, 그건 k값의 범위와 동일

while start <= end:
    mid = (start+end)//2  # 어떤 수 x

    temp = 0  # 작거나 같은 수의 개수
    for i in range(1, n+1):
        temp += min(mid//i, n)  # 왜 인덱스에서 x값을 설정하는 걸까? -> 찾아야 하는 값이 숫자이기 때문에

    if temp >= k:  # 조건을 만족하는 가장 큰 수를 찾아냄
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
