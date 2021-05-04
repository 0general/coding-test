# 수정 요망

def solution(s):
    n = int(len(s)/2)
    answer = 0
    min_value = len(s)
    plus = 0
    for i in range(1, n+1):
        dap = ''
        f_index = 0
        while f_index < n:
            check = s[f_index:f_index+i-1]
            g = s[f_index+i:]
            if len(g) < len(check):
                dap += g
            else:
                n_index = g.find(check)
                if n_index == -1:
                    dap += check
                    f_index = n_index+i
                    if len(dap) > min_value:
                        break

                else:
                    plus = int((n_index-f_index)/i) + 1
                    dap = dap + str(plus) + check
                    f_index = n_index+i
                    if len(dap) > min_value:
                        break

        if len(dap) < min_value:
            min_value = len(dap)
    answer = len(dap)
    return answer
