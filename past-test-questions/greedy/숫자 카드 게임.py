'''
2019 국가 교육기관 코딩 테스트

- N행 M열 카드 배열
- 뽑고자 하는 카드가 포함된 행 선택
- 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드 선택
- 뽑은 카드가 각 행에 포함된 가장 낮은 숫자들 중 가장 큰 숫자여야 한다. 

N과 M은 1이상 10000이하의 자연수

ex)
N, M = 3, 4
[[2,3,4,5],[8,1,3,4],[5,6,4,5]]
이면 4를 출력해야 한다.

'''
'''

result = 0
for in in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


'''
'''

result = 0
for i in range(n):
    data = list(map(int, input().spllit()))
    min_value = 10001 #입력가능한 최대 수가 10000이니까
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)

'''


def choose(N, M, data):
    row = []
    for i in range(N):
        row.append(min(data[i]))

    print("뽑은 숫자 : ", max(row))


n, m = map(int, input("N행 M열을 설정하시오 : ").split())

data = []
for j in range(n):
    while 1:
        check = list(map(int, input('한 행을 입력하시오 : ').split()))
        if len(check) == m:
            break
    data.append(check)

choose(n, m, data)
