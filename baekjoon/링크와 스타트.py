"""
https://www.acmicpc.net/problem/15661
"""
import sys


def team_make_BT(idx, team):
    if idx >= n or len(team) > n//2:
        return
    team_make_BT(idx+1, team)
    if len(team) < n//2:  # 스타트팀이 아니라면 링크 팀이므로 팀이 두 개로 나눠지는 구성이 똑같아지지 않도록 조건 추가
        t = team + [idx]
        all_team.append(t)
        team_make_BT(idx+1, t)


input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

mini = 40000
all_team = []
team_make_BT(0, [])
for team in all_team:
    abl = 0
    link = [i for i in range(n) if i not in team]  # 이 팀에 해당되지 않는다면 다른 팀에 속함
    for i in range(len(team)-1):  # 첫 번째 팀 능력치 합산
        for j in range(i+1, len(team)):
            abl += arr[team[i]][team[j]] + arr[team[j]][team[i]]
    for x in range(len(link)-1):  # 두 번째 팀 능력치 합산
        for y in range(x+1, len(link)):
            abl -= arr[link[x]][link[y]] + arr[link[y]][link[x]]
    abl = abs(abl)
    if abl < mini:
        mini = abl
    if mini == 0:  # 최소값은 0이 가장 작다
        break

print(mini)
