import sys
sys.stdin = open("input.txt")

arr = [list(map(int, input().split(' '))) for _ in range(9)]

for i in range(len(arr)):
    if i % 2 :
        for j in range(len(arr[0])-1, -1, -1):
            print(arr[i][j], end=' ')
    else:
        for j in range(len(arr[0])):
            print(arr[i][j], end=' ')
    print()

    ## 첫번째 줄은 -> 방향으로
    ## 두번째 줄을 <- 방향으로 탐색색