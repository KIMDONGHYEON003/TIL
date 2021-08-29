import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
arr = list(map(int, input().split()))
result = []
for date in range(N-K+1):
    result.append(sum(arr[date:date+K]))

print(max(result))