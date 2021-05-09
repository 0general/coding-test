def solution(s):
    n = len(s)
    answer = n
    for i in range(1, (n//2)+1):  # 검사 단위 i
        j = 0
        cnt = 1
        check = ''
        temp = ''
        for _ in range(n//i):  # 검사 시작
            if temp == s[j:j+i]:
                cnt += 1
                j += i
            else:
                if cnt == 1:
                    check += temp
                else:
                    check = check + str(cnt) + temp
                    cnt = 1
                temp = s[j:j+i]
                j += i
        if cnt == 1:
            check += temp
        else:
            check = check + str(cnt) + temp
        if j < n:
            check += s[j:]
        answer = min(len(check), answer)
    return answer
