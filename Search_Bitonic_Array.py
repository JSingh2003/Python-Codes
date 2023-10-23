def Bitonic_Point(arr):
    low = 0
    high = len(arr) -1
    while high > low:
        mid = (low + high)//2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            low = mid +1
        else:
            high = mid - 1

def Bitonic_Search(arr,p,key):
    if arr[p] == key:
        return p
    a1 = arr[0:p+1]
    a2 = arr[p+1:]
    l1 = 0
    h1 = p
    l2 = 0
    h2 = len(arr) - p - 2

    while (h1 >= l1) or (h2 >= l2):
        if h1 >= l1:
            mid = (h1 + l1)//2
            if a1[mid] == key:
                return mid
            elif a1[mid] < key:
                l1 = mid +1
            else:
                h1 = mid-1

        if h2 >= l2:
            mid = (h2 + l2)//2
            print(l2,mid,h2,a2[mid],key)
            if a2[mid] == key:
                return p + mid + 1
            elif a2[mid] < key:
                h2 = mid - 1
            else:
                l2 = mid + 1

    return -1     
array = [-3, 3, 7, 9, 11, 23, 22, 18, 15, 10, 6]
p = Bitonic_Point(array)
key = 18
ans = Bitonic_Search(array,p,key)

if ans == -1:
    print(key,"Not in the Array")
else:
    print(ans)