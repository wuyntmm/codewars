def checker(n, test):
    n = list(str(n))
    for i in list(str(test)):
        if i in n:
            n.remove(i)
        else:
            return False
    return True


def next_bigger(n):
    if str(n) == ''.join(sorted(list(str(n)), reverse=True)):
        return -1
    for i in range(n + 1, int('9' * len(str(n)))):
        if checker(n, i):
            return i
    return -1


print(next_bigger(6543212))
