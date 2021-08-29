import sys
sys.stdin = open("input.txt")

C , R = list(map(int,input().split()))
Key = int(input())
arr = [[0 for _ in range(R)] for _ in range(C)]

di = [0, 1, -1, 0]
dj = [1, 0, 0, -1]

i, j = 0, -1
k = 0
res = 1


while res != Key:
    nx, ny = i + di[k], j + dj[k]
    if 0 <= nx < C and 0 <= ny < R:
        if arr[nx][ny] == 0:
            arr[nx][ny] = res
            res += 1
            i, j = nx, ny
        else:
            k += 1
            if k == 4:
                k = 0
    else:
        if nx < 0 and nx >= R:
            nx -= 1
        else:
            ny -= 1
        k += 1
        if k == 4:
            k = 0

    if res == Key:
        nx, ny = i + di[k], j + dj[k]
        print(nx+1, ny+1)
        break
    if res > C*R:
        print(0)
        break












