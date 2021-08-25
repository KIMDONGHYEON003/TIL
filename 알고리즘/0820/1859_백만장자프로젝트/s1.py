import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    bns = map(int, input())
    result = 0

    for i in range(N):
        max_sell = 0
        for j in range(i+1, N):
            if bns[i] - bns[j] >= 0 and max_sell < bns[i] - bns[j]:
                max_sell = bns[i] - bns[j]
        result += max_sell