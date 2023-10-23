def Three_Sum(arr):
    n = len(arr)
    arr.sort()
    sol=[]
    for i in range(n-2):
        x = arr[i]
        left = i + 1
        right = n -1

        while left < right:
            total = x + arr[left] + arr[right]

            if total == 0:
                sol.append([x,arr[left],arr[right]])
                left += 1
                right -= 1
            elif total < 1:
                left += 1
            else:
                right -= 1
    return sol

array = [-2,4,2,-3,1,-2,0]
ans = Three_Sum(array)
if ans != []:
    print(ans)
else:
    print("Their is no 3-Sum solution")