# 1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N


def powerset(idx):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx] = 0
        powerset(idx + 1)


powerset(0)


# 2.
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []


def powerset(idx):
    if idx < N:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx] = 0
        powerset(idx + 1)
    else:
        total = 0
        for i in range(N):
            if sel[i]:
                total += arr[i]

        if total == 10:
            for i in range(N):
                if self[i]:
                    print(arr[i], end=" ")


powerset(0)
