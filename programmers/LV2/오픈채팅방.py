def solution(record):
    answer = []
    command = ["Enter", "Leave", "Change"]
    dict = {}
    record = [x.split() for x in record]
    for st in record:
        if len(st) > 2:
            dict[st[1]] = st[2]
    for st in record:
        if st[0] == command[0]:
            answer.append("%s님이 들어왔습니다." % dict[st[1]])
        elif st[0] == command[1]:
            answer.append("%s님이 나갔습니다." % dict[st[1]])
    return answer
