import sys
sys.stdin = open("input.txt")

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]
graph = [[0 for _ in range(100)] for _ in range(100)]
result = 0

for arr in array:
    for i in range(arr[1], arr[1]+10):
        for j in range(arr[0], arr[0] + 10):
            graph[i][j] = 1

for g in graph:
    result += g.count(1)
print(result)