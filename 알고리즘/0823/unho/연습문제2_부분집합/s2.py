#2. Justin 교수님
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []

def powerset(idx):
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

    else:
        total = 0
        for i in range(N):
            if sel[i]:
                total += arr[i]
        if total == 10:
            for i in range(N):
                if sel[i]:
                    print(arr[i], end=' ')
            print()

powerset(0)



#2. 내가 작성 (마지막 요소 포함이 안됨 수정 필요)
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []

def powerset(idx, s):
    #Base Case
    if idx == N:
        return
    elif s == 10:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
    elif s > 10:
        return
    else:
        sel[idx] = 1
        powerset(idx+1, s+arr[idx])
        sel[idx] = 0
        powerset(idx+1, s)

powerset(0, 0)