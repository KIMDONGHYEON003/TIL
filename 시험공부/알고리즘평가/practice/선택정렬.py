arr = [1,5,25,3,58,4,5,21,216,1,5,10]

def solution(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr

print(solution(arr))