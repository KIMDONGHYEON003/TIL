arr = [1,5,25,3,58,4,5,21,216,1,5,10]

def BubbleSort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(BubbleSort(arr))
print(sorted(arr))

