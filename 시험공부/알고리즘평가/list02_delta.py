import sys
sys.stdin = open("input.txt")

dx = [0,0,-1,1]
dy = [-1,1,0,0]

arr = [list(map(int, input().split(' '))) for _ in range(9)]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for I in range(4): # 총 네 방향에 접근할 것이다.
            textX = x+dx[I]
            textY = y+dy[I]
            if 0 <= textX < len(arr) and 0 <= textY <= len(arr[x]):
                print(arr[textX][textY])