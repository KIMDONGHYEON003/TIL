arr = [1,5,25,3,58,4,5,21,216,1,5,10]

N = len(arr)

for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end=' ')
    print()

