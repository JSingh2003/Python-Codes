def Selection_Sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return(arr)

array=[2,3,10,9,-2,0,4]
print(Selection_Sort(array))