'''
https://www.acmicpc.net/problem/1339
'''
n = int(input())  # 단어 수학

word = [list(input()) for _ in range(n)]
word.sort(key=len, reverse=True)

num = len(word[0])  # 자리수
answer = [[] for _ in range(num)]

for i in range(n):  # answer에 자리수 별로 덧셈
    for j in range(-1, -len(word[i])-1, -1):
        answer[j].append(word[i][j])

dic = dict()
# 자릿수 별로 구분된 answer 리스트 완성
for i in range(num):  # 곱해줄 자릿수 계산 10**num-1-i
    for j in answer[i]:
        if j not in dic:
            dic[j] = 10**(num-1-i)
        else:
            dic[j] += 10**(num-1-i)

answer = sorted(dic.items(), key=lambda x: x[1], reverse=True)
s = 9
sum = 0
for i in answer:
    sum += i[1]*s
    s -= 1
print(sum)
