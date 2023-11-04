def partition(arr,low,high):
    pivot = arr[high]
    x = low
    for i in range(low,high):
        if arr[i] <= pivot:
            arr[x], arr[i] = arr[i], arr[x]
            x += 1
    arr[x], arr[high] = arr[high], arr[x]
    return x

def QuickSort(arr,low,high):
    if low < high:
        x = partition(arr,low,high)
        QuickSort(arr,low,x - 1)
        QuickSort(arr,x,high)

array = [2, 3, 10, 19, 9, -2, 0, 4]
QuickSort(array, 0, len(array) - 1)
print(array)