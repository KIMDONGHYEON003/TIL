import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
res = [i for i in range(1, N+2)]

for i in range(len(arr)):
    if arr[i] >= 1:
        if i - arr[i] >= 0 :
            res[i] , res[-1] = res[-1], res[i]
            for k in range(len(res)-3, len(res)-3-arr[i], -1):
                res[i- 1], res[i] = res[i], res[i - 1]
            res[-1], res[len(res) - 2 - arr[i]] = res[len(res) - 2 - arr[i]], res[-1]
        else:
            for k in range(len(res)-3, -1, -1):
                res[i - 1], res[i] = res[i], res[i - 1]
            res[-1], res[0] = res[0], res[-1]


for i in res:
    print(i, end=" ")



