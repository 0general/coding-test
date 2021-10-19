"""
https://www.acmicpc.net/problem/1182
"""


def BT(idx, hap, string):  # 현재 인덱스 위치, 합
    if hap == s:  # 만족했더라도 뒤 원소에 0이 포함된 경우를 고려해야 하므로 종료해서는 안됨.
        # 주의할 점 : 뒤까지 가봤는데 0이나 추가된 수가 없는 경우 중복해서 카운팅 된다.
        ans.add(string)
    if idx >= n:  # 인덱스 범위를 벗어나면 종료
        return
    # num은 정렬되어있으므로 idx 이후로는 모두 현재 숫자보다 큰 수가 나온다.
    if hap >= s and num[idx] > 0:
        return
    # num의 값으로 넣으면 구분이 안되므로 index를 넣는다. 숫자 겹침 구분용
    BT(idx+1, hap+num[idx], string+"/"+str(idx))
    BT(idx+1, hap, string)


n, s = map(int, input().split())

num = list(map(int, input().split()))
num.sort()
ans = set()
BT(0, 0, "")
ans.discard('')  # s가 0인 경우 공집합이 들어갈 수 있다.
print(len(ans))
