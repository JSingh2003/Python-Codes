from random import randint

def Knuth_Shuffle(arr):
    for i in range(len(arr)):
        j = randint(0,i+1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

array=[2,3,10,9,-2,0,4]
print(Knuth_Shuffle(array))  