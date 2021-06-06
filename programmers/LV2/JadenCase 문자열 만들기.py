def solution(s):
    answer = ''
    s = s.lower()
    # split()을 default를 이용한다면 공백이 여러개인 것을 모두 없애버리기에 split(" ")와 달라진다.
    s = s.split(" ")
    for i in s:
        i = i.capitalize()
        answer += i+" "
    return answer[:-1]


'''
다른 풀이

def solution(s):
    s = s.lower()
    s = list(s)
    answer = ' '
    for i in s:
        if answer[-1] == ' ': answer += i.upper()
        else: answer += i
    return answer[1:]
'''
