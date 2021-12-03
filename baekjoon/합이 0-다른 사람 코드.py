"""
125964	448	PyPy3
이정도밖에 안 걸림. 신기하니까 연구해보자 -> 연구 완료
https://www.acmicpc.net/user/woojerry 이 사람이 푼 방식
"""

import sys

read = sys.stdin.readline
N = int(read())
skills = sorted(list(map(int, read().rstrip().split())))
count = 0
skill_sum = 0

for pick in range(N):
    if skills[pick] > 0:  # 정렬돼있으므로
        break
    start, end = pick + 1, N-1  # 사용하려는 수가 pick이 기준 start와 end를 모두 이용, 투 포인터
    j = N
    while start < end:  # 애초에 start와 end가 다른 조건이므로
        skill_sum = skills[pick] + skills[start] + skills[end]
        if skill_sum == 0:  # 찾아야 하는 경우
            if skills[start] == skills[end]:  # left와 right가 서로 같을 때 #  start와 end가 같은 수라면
                # 같은 수의 범위 내에서 계산 = N(N-1)//2
                count += (end - start + 1)*(end - start) // 2
                break

            else:  # 서로 같지 않다면
                start_same, end_same = 0, 0  # 중복되는 수의 개수 찾기
                start_data, end_data = skills[start], skills[end]
                while True:
                    if skills[end] == end_data:
                        end_same += 1
                        end -= 1
                    else:
                        break
                while True:
                    if skills[start] == start_data:
                        start_same += 1
                        start += 1
                    else:
                        #start += 1
                        break
                count += start_same * end_same

        elif skill_sum > 0:
            end -= 1
        else:
            start += 1
print(count)
