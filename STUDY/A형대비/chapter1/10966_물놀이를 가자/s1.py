import sys
sys.stdin = open("input.txt")

from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    checked = [[-1] * M for _ in range(N)]
    board = [[i for i in input()] for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                queue.append((i, j))
                checked[i][j] = 0

    while queue:
        ni, nj = queue.popleft()    # queue에서 ni nj
        for idx in range(4):
            x, y = ni + di[idx], nj + dj[idx]   # 이동
            if x in range(N) and y in range(M): # 바깥에 안나가기 위해
                if checked[x][y] == -1: # L인 경우
                    queue.append((x, y))
                    checked[x][y] = checked[ni][nj] + 1 # 전 칸에서 한칸 더 가야하기 때문에 +1

    result = 0
    for i in checked:   # 모든 이동횟수의 합을 구해야함
        result += sum(i)

    print("#{} {}".format(t+1, result))