import sys
sys.stdin = open("input.txt")

from collections import deque

def way(r, c):
    queue = deque()
    queue.append((r, c))
    checked[r][c] = 1
    dr = [1, -1, 0, 0]  # 하,상,좌,우
    dc = [0, 0, -1, 1]
    # p_pipe는 위치가 바뀔 때 연결되는 2번째 파이프
    # b_pipe는 현재 위치
    # 순서는 하 상 좌 우
    a_pipe = [[1, 2, 5, 6], [1, 2, 4, 7], [1, 3, 6, 7], [1, 3, 4, 5]]
    b_pipe = [[1, 2, 4, 7], [1, 2, 5, 6], [1, 3, 4, 5], [1, 3, 6, 7]]
    
    while queue:
        v = queue.popleft()
        r, c = v[0], v[1]
        for i in range(4):
            x, y = r + dr[i], c + dc[i]
            if x in range(N) and y in range(M):
                if checked[x][y] == 0:
                    if pipe[r][c] in a_pipe[i] and pipe[x][y] in b_pipe[i]:
                        queue.append([x, y])
                        checked[x][y] = checked[r][c] + 1

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    pipe = [[i for i in map(int, input().split())] for _ in range(N)]
    checked = [[0 for _ in range(M)] for _ in range(N)]
    result = 0
    way(R, C)
    for i in checked:
        for j in i:
            if j > 0 and j <= L:
                result += 1
    print("#{} {}".format(t+1, result))
