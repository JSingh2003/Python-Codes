def Merge(arr, l, m, r):
    l1 = []
    l2 = []

    for i in range(m - l + 1):
        l1.append(arr[l + i])

    for i in range(r - m):
        l2.append(arr[m + i + 1])
    i, j, k = 0, 0, l
    while i < m - l + 1 and j < r - m:
        if l1[i] <= l2[j]:
            arr[k] = l1[i]
            i += 1
        else:
            arr[k] = l2[j]
            j += 1
        k += 1

    while i < m - l + 1:
        arr[k] = l1[i]
        i += 1
        k += 1

    while j < r - m:
        arr[k] = l2[j]
        j += 1
        k += 1

def Merge_Sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        Merge_Sort(arr, l, m)
        Merge_Sort(arr, m + 1, r)
        Merge(arr, l, m, r)

array = [2, 3, 10, 19, 9, -2, 0, 4]
Merge_Sort(array, 0, len(array) - 1)
print(array)