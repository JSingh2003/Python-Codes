def Shell_Sort(arr):
    gap=len(arr)//2

    while gap > 0:
        i = gap

        while i < len(arr):
            j = i - gap

            while j >= 0:

                if arr[j + gap] > arr[j]:
                    break
                else:
                    arr[j + gap], arr[j] = arr[j], arr[j + gap]
                
                j -= 1
            
            i += 1
        gap // 2

array=[2,3,10,9,-2,0,4]
print(Shell_Sort(array))