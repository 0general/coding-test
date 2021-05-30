def solution(clothes):
    answer = 1
    type = []
    dict = {}
    for i in clothes:
        if i[1] not in type:
            type.append(i[1])
    for j in type:
        dict[j] = 0
    for i in clothes:
        dict[i[1]] += 1
    for k in type:
        answer *= (dict[k] + 1)
    return answer - 1
