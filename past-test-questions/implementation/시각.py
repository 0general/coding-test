'''
데이터의 수가 100만 개 이하일 때 완전 탐색을 사용하면 적절

하루 24시간은 86400초로 모든 초를 검사해도 검사해야 할 데이터의 수가 10만 개를 넘지 않는다.
'''
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
