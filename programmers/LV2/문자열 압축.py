
def solution(s):
    answer = 0
    min_value = len(s)

    for i in range(1, len(s)//2 + 1):  # i는 묶음 단위
        dap = ''
        f = 0
        n = f+i
        cnt = 1
        # 검사할 문장
        while n < len(s):
            temp = s[f:f+i]
            print("비교 대상 : ", temp)
            if n+i <= len(s):
                b = s[n:n+i]
                print("인덱스 위치 : ", n, "확인 대상 : ", b, "\n--------------------")
                if temp == b:
                    cnt += 1
                else:
                    if cnt == 1:
                        dap += temp
                        print(dap)
                        f = n
                    else:
                        dap = dap + str(cnt) + temp
                        print(dap)
                        cnt = 1
                        f = n
            else:
                dap += s[n:]
                print("처음 : ", s, "종료 : ", dap)
                break
            n += i
        if min_value > len(dap):
            min_value = len(dap)

    answer = min_value
    return answer


solution('aabbacc')
