import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
res = []
tmp = []
cnt = 0
for i in range(len(arr)):
    cnt += 1
    if arr[i] >= 1:
        if i - arr[i] >= 0:
            for _ in range(arr[i]):
                tmp.append(res.pop(-1))
            res.append(cnt)
            for _ in range(len(tmp)):
                res.append(tmp.pop(-1))
        else:
            for _ in range(len(res)):
                tmp.append(res.pop(-1))
            res.append(cnt)
            for _ in range(len(tmp)):
                res.append(tmp.pop(-1))
    elif arr[i] == 0:
        res.append(cnt)

for i in range(len(res)):
    print(res[i], end=" ")
