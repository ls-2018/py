def findCommon(a, b, c):
    i = j = k = 0
    n1 = len(a)
    n2 = len(b)
    n3 = len(c)
    while i < n1 and j < n2 and k < n3:
        if a[i] == b[j] == c[k]:
            print(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1


if __name__ == '__main__':
    arr1 = [2, 5, 12, 20, 45, 85]
    arr2 = [16, 19, 20, 85, 200]
    arr3 = [3, 4, 15, 20, 39, 72, 85, 190]
    findCommon(arr1, arr2, arr3)
