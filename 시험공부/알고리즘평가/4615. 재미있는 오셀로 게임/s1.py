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

    for x in range(N):
        for y in range(N):
            for k in range(8):
                nx, ny = x + di[k], y + dj[k]
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0 and arr[nx][ny] != b:
                    a = 0
                    stack = []
                    while arr[nx+di[k]*a][ny+dj[k]*a] == b:
                        stack.append(a)
                        a += 1
                        if 0 <= nx+di[k]*a < N and 0 <= ny+dj[k]*a < N:
                            if arr[nx+di[k]*a][ny+dj[k]*a] != 0 and arr[nx+di[k]*a][ny+dj[k]*a] == b:
                                for m in stack:
                                    if k == 0:
                                        arr[nx + di[k] * a + m][ny + dj[k] * a] = b
                                    elif k == 1:
                                        arr[nx + di[k] * a - m][ny + dj[k] * a] = b
                                    elif k == 2:
                                        arr[nx + di[k] * a][ny + dj[k] * a + m] = b
                                    elif k == 3:
                                        arr[nx + di[k] * a][ny + dj[k] * a - m] = b
                                    elif k == 4:
                                        arr[nx + di[k] * a + m][ny + dj[k] * a + m] = b
                                    elif k == 5:
                                        arr[nx + di[k] * a + m][ny + dj[k] * a - m] = b
                                    elif k == 6:
                                        arr[nx + di[k] * a - m][ny + dj[k] * a + m] = b
                                    elif k == 7:
                                        arr[nx + di[k] * a - m][ny + dj[k] * a - m] = b



    print(arr)


