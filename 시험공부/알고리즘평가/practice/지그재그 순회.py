from pandas import DataFrame
N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
cnt = 1

for i in range(len(arr)):
    if i % 2 == 0:
        for j in range(len(arr[i])):
            arr[i][j] = cnt
            cnt += 1
    else:
        for j in range(len(arr[i])-1, -1, -1):
            arr[i][j] = cnt

            cnt += 1

print(DataFrame(arr))