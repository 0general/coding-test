'''
https://www.acmicpc.net/problem/11399
'''
n = int(input())  # 사람 수
time = sorted(list(map(int, input().split())))
for i in range(1, n):
    time[i] += time[i-1]
print(sum(time))
