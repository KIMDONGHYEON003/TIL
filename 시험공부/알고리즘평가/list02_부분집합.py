# 집합의 원소가 n개 일 때, 공집합을 포함한 부분집합의 수는 2**n 개이다.
# 부분집합 생성하기
# bit = [0,0,0,0]
#
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit, end=' ')
#
#                 for p in range(4):
#                     if bit[p]:
#                         print(bit[p], end=' ')
#                 print()

# 부분집합\
arr = [1, 5, 25, 3, 58, 4, 5, 21, 216, 1, 5, 10]
N = len(arr)
result2 = []
for i in range(1, 1 << N):
    result1 = []
    for j in range(N):
        if i & (1 << j):
            result1.append(arr[j])
    result2.append(result1)

for i in result2:
    print(i)

