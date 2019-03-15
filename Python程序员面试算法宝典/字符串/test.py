
def test(demo='abaabc'):
    i = 0
    j = -1
    array = [0] * (len(demo) + 1)
    while i < len(array):
        if list(demo)[i] == list(demo)[j]:
            i += 1
            j += 1
            array[i] = j
        else:
            j = array[j]

test()