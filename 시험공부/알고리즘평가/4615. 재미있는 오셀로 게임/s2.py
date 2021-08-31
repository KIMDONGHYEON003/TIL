import sys
sys.stdin = open("input.txt")

di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())

for t in range(T):
    N, M = list(map(int, input().split()))
    arr = [[0 for _ in range(N)] for _ in range(N)]
    k = 0
    for _ in range(M):
        x, y, b = list(map(int, input().split()))
        arr[x-1][y-1] = b

        for k in range(8):
            nx, ny = (x-1) + di[k], (y-1) + dj[k]
            a = 0
            stack = []
            while True:
                if 0 <= nx+di[k]*a < N and 0 <= ny+dj[k]*a < N:
                    if arr[nx+di[k]*a][ny+dj[k]*a] == 0:
                        stack = []
                        break
                    elif arr[nx+di[k]*a][ny+dj[k]*a] == b:
                        break
                    else:
                        stack.append([nx+di[k]*a, ny+dj[k]*a])
                else:
                    stack = []
                    break
                a += 1
            for s in stack:
                arr[s[0]][s[1]] = b

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            else:
                white += 1
    print("#{} {} {}".format(t+1, black, white))


