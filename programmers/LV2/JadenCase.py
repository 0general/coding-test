def solution(s):
    answer = ''
    s = s.lower()
    s = s.split(" ")
    for i in s:
        i = i.capitalize()
        answer += i+" "
    return answer[:-1]
