def Insertion_Sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
            else:
                break
    return(arr)

array=[2,3,10,9,-2,0,4]
print(Insertion_Sort(array))