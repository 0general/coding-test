def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        n, m = len(phone_book[i]), len(phone_book[i+1])
        if n > m:
            continue
        else:
            if phone_book[i+1][:n] == phone_book[i]:
                return False
    return True
