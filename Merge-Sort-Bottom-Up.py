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

def Merge_Sort_Bottom_Up(arr):
    i=1
    while i < len(arr):
        j=0
        while j < len(arr) - 1:
            Merge(arr,j,j+i-1, min(j+2*i-1, len(arr)-1))
            j += 2*i
        i = 2*i

array=[2,3,10,9,-2,0,4]
(Merge_Sort_Bottom_Up(array))
print(array)