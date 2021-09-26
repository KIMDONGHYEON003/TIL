import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(1, T+1):
    N = int(input())
    arr = []
    cnt = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j = 0, -1
    k = 0
    while cnt <= N * N:     # 전체 모두 정렬하면 끝나도록
        ni, nj = i + di[k], j + dj[k]       # 델타 값 만큼 더해주면서 방향을 바꾼다
        if arr[ni][nj] and arr[ni][nj] == 0:    # arr[ni][nj]가 존재하고 and 0이랑 같은 경우
            arr[ni][nj] = cnt               # 하나씩 넣어준다.
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4         # 꼭 기억하기

    print("#{} {}".format(num, arr))