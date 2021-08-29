import sys
sys.stdin = open("input.txt")

arr = list(map(int, input().split()))

for i in range(len(arr)-1, -1, -1):
    for j in range(0,i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
