'''
https://www.acmicpc.net/problem/11054
'''
n = int(input())  # 수열의 크기
num = list(map(int, input().split()))

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if num[i] > num[j]:
            increase[i] = max(increase[j]+1, increase[i])
        if num[-i-1] > num[-j-1]:
            decrease[-i-1] = max(decrease[-j-1]+1, decrease[-i-1])

result = [increase[i] + decrease[i]-1 for i in range(n)]
print(max(result))
