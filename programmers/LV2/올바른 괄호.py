
def solution(s):
    answer = True
    list = []

    for i in s:
        if i == '(':
            list.append(i)
        else:
            if len(list) == 0:
                return False
            list.pop()
    if len(list) != 0:
        return False
    return answer
