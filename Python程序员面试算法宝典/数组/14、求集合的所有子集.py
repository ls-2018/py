def func_1(array, mask, c):
    length = len(array)
    if length == c:
        print('{', end='')
        i = 0
        while i < length:
            if mask[i] == 1:
                print(array[i], end='')
            i += 1
        print("}")
    else:
        mask[c] = 1
        func_1(array, mask, c + 1)
        mask[c] = 0
        func_1(array, mask, c + 1)


def func_2(array):
    if array is None or len(array) < 1:
        print('参数不合法')
        return
    _arr = list(array[0])
    i = 1
    while i < len(array):
        lens = len(_arr)
        j = 0
        while j < lens:
            temp = _arr[j] + array[i]
            _arr.append(temp)
            j += 1
        _arr.append(array[i])
        i += 1
    return _arr


'''
把我当成 是从大
'''

if __name__ == '__main__':
    arr = ['a', 'b', 'c']
    mask = [0, 0, 0]
    func_1(arr, mask, 0)
    print('----------------------------------------------')
    print(func_2(arr))
# 14、求集合的所有子集
