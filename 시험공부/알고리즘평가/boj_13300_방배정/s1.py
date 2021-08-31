import sys
sys.stdin = open("input.txt")

N, K = list(map(int, input().split()))
info_list = [list(map(int,input().split())) for _ in range(N)]
boy = [0] * 7
girl = [0] * 7
for info in info_list:

    if info[0] == 1:
        boy[info[1]] += 1
    else:
        girl[info[1]] += 1

result = 0
for i in range(1, 7):

    if boy[i] % K == 0:
        result += boy[i] // K
    else:
        result += boy[i] // K + 1

    if girl[i] % K == 0 :
        result += girl[i] // K
    else:
        result += girl[i] // K + 1

print(result)
