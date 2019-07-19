a = [1, 2, 6, 4, 3, 6, 3, 2, 6, 9, 8]
for i in range(0, 11):
    for j in range(i, 11):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)
