'''
2019 국가 교육기관 코딩 테스트

첫째 줄 :
- N(2<=N<=1000), M(1<=M<=1000), K(1<=K<=10000)
N, M, K는 공백으로 구분

둘째 줄 :
- N개의 자연수
각 자연수는 공백으로 구분, 각 자연수는 1 이상 10000이하의 수

K는 M보다 항상 작거나 같다.
K<=M

특별한 큰 수의 법칙 : 
특정한 배열의 수를 M번 더하여 가장 큰 수를 출력하라.
K는 특정한 인덱스의 수가 연속으로 더해질 수 있는 숫자를 의미한다. 
'''

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

count = int(m/(k+1))
count += m%(k+1)

result = data[0]*count
result += data[0]*(m-count)

print(result)

