'''
효율성 테스트 통과 실패

def solution(people, limit):
    answer = 0  # 구명보트의 개수 최솟값
    # 몸무게를 담은 배열 people
    # 구명보트의 무게 제한 limit

    people.sort()
    while True:
        hap = 0
        n = len(people)  # 남은 사람 수
        if n == 0:
            break
        hap += people[n-1]
        for i in range(n-2, -1, -1):
            if hap + people[i] <= limit:
                people.pop(i)
                break
        people.pop()
        answer += 1

    return answer

'''


def solution(people, limit):
    n = len(people)
    answer = 0
    people.sort()
    i, j = 0, n-1
    while i <= j:
        if i == j:
            answer += 1
            break
        sum = people[i] + people[j]
        if sum > limit:
            answer += 1
            j -= 1
        else:
            answer += 1
            i, j = i+1, j-1

    return answer
