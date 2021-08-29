import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int, input().split()))
result = 1
down = 1
up = 1

for i in range(1, len(arr)):
    if arr[i-1] <= arr[i]:
        up += 1
        if up > result:
            result = up
    else:
        up = 1

for i in range(1, len(arr)):
    if arr[i-1] >= arr[i]:
        down += 1
        if down > result:
            result = down
    else:
        down = 1

print(result)