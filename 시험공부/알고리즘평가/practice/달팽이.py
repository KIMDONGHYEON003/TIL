import sys
sys.stdin = open("input1.txt")
from pandas import DataFrame

T = int(input())
for num in range(T):
    N = int(input())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 1
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    i,j = 0, -1
    k = 0
    while cnt <= N*N:
        ni, nj = i + di[k], j + dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4

    print(DataFrame(arr))
