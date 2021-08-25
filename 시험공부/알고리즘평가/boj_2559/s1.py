import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
arr = list(map(int, input().split()))
result = []
for date in range(N-K+1):
    d_sum = 0
    for k in range(date, date+K):
        d_sum += arr[k]
    result.append(d_sum)

print(max(result))
