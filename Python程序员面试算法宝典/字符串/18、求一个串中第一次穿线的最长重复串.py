def getMax(strs):
    maxlen = 1
    lens = len(strs)
    start = 0
    end = 0
    for i in range(lens):
        j = i
        while j <= lens - 2:
            if list(strs)[j + 1] != list(strs)[j]:
                break
            j += 1
            if maxlen < j - i + 1:
                maxlen = j - i + 1
                start = i
                end = j
    print(strs[start:end + 1])
    return maxlen


if __name__ == '__main__':
    s = 'aaabbbccccdsssssss'
    print(getMax(s))
