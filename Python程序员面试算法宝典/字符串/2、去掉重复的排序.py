def swap(str, i, j):
    tmp = str[i]
    str[i] = str[j]
    str[j] = tmp


def isDup(str, begin, end):
    i = begin
    while i < end:
        if str[i] == str[end]:
            return False
        i += 1
    return True


def permutation(str, start):
    if str is None or start < 0:
        return
    if start == len(str) - 1:
        print(''.join(str))
    else:
        i = start
        while i < len(str):
            if not isDup(str, start, i):
                i += 1
                continue
            swap(str, start, i)
            permutation(str, start + 1)
            swap(str, start, i)
            i += 1


if __name__ == '__main__':
    s = list('aabc')
    permutation(s, 0)
