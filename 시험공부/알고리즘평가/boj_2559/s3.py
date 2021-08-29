import sys
sys.stdin = open("input.txt")

N, K = map(int,input().split())
arr = list(map(int, input().split()))
result = []
tmp = []

for i in range(K):
    tmp.append(arr[i])
result.append(list(tmp))


for j in range(K,N):
    del tmp[0]
    tmp.append(arr[j])

    result.append(tmp)

print(max(result))