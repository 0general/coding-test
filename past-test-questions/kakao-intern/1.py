import re


def solution(s):
    answer = ''
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    check = list(s)
    i = 0
    while i < len(check):
        if check[i] not in num:
            if check[i] == 'z':
                answer += '0'
                i += 3
            elif check[i] == 'o':
                answer += '1'
                i += 2
            elif check[i] == 't':
                if check[i+1] == 'w':
                    answer += '2'
                    i += 2
                else:
                    answer += '3'
                    i += 4
            elif check[i] == 'f':
                if check[i+1] == 'o':
                    answer += '4'
                    i += 3
                else:
                    answer += '5'
                    i += 3
            elif check[i] == 's':
                if check[i+1] == 'i':
                    answer += '6'
                    i += 2
                else:
                    answer += '7'
                    i += 4
            elif check[i] == 'e':
                answer += '8'
                i += 4
            else:
                answer += '9'
                i += 3
        else:
            answer += check[i]
        i += 1
        if i >= len(check):
            break

    return int(answer)
