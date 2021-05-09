def solution(n, k, cmd):  # 표의 행 개수 n, 선택된 행의 위치 k, 수행한 명령어들이 담긴 문자열 배열 cmd
    answer = ['O' for _ in range(n)]
    dels = []
    ans = ''
    for i in cmd:

        if i == "C":
            answer[k] = 'X'
            dels.append(k)
            if k == n-1:
                for i in range(n-2, -1, -1):
                    if answer[i] != "X":
                        k = i
                        break
            else:
                for i in range(k+1, n):
                    if answer[i] != "X":
                        k = i
                        break
        elif i == "Z":
            p = dels.pop()
            answer[p] = "O"
        else:
            h = i.split()
            if h[0] == "U":
                count = 0
                while count < int(h[1]):
                    # if k == 0: break
                    k -= 1
                    if answer[k] == "X":
                        continue
                    count += 1
            else:
                count = 0
                while count < int(h[1]):
                    if k == n-1:
                        break
                    k += 1
                    if answer[k] == "X":
                        continue
                    count += 1
    for i in answer:
        ans += i
    return ans
