import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split()))

bridges = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    a, b, c = map(int, input().split())
    bridges[a][b] = max(bridges[a][b], c)
    bridges[b][a] = max(bridges[b][a], c)

fac1, fac2 = map(int, input().split())
print(bridges[fac1][fac2])