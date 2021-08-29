arr = [[7, 3, 6, 4, 2],[5, 8, 9, 1, 6],[2, 1, 4, 5, 8],[8, 4, 7, 9, 3],[1, 5, 3, 8, 4]]
result = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i and j != 0 and i and j != len(arr[i])-1:
            result += abs(arr[i-1][j]-arr[i][j]) + abs(arr[i+1][j]-arr[i][j]) + abs(arr[i][j-1]-arr[i][j]) + abs(arr[i][j+1]-arr[i][j])
        elif i == 0 and j == 0:
            result += abs(arr[i+1][j]-arr[i][j]) + abs(arr[i][j+1]-arr[i][j])
        elif i == 0 and j != 0 and j != len(arr[i])-1:
            result += abs(arr[i + 1][j] - arr[i][j]) + abs(arr[i][j-1] - arr[i][j]) + abs(arr[i][j+1] - arr[i][j])
        elif i != 0 and j == 0 and i != len(arr[i])-1:
            result += abs(arr[i + 1][j] - arr[i][j])+abs(arr[i -1][j] - arr[i][j])+abs(arr[i][j+1] - arr[i][j])
        elif 


