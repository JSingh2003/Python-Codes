def Binary_Search(arr,key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while(high >= low):
        mid = (high + low)//2
        if key == arr[mid]:
            return mid
        if key < arr[mid]:
            high = mid 
        elif key > arr[mid]:
            low = mid
    return -1

arr = [ 2, 3, 9, 14, 30, 60 ]
x = 14
arr.sort() 
result = Binary_Search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")