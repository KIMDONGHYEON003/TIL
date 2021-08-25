#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]    # 전체 집합(요소)
N = len(arr)       # 해당 집합의 요소 수
sel = [0] * N      # 해당 요소를 선택/ 선택하지 않음을 표현하는 배열

# [0, 0, 0]

def powerset(idx):
    if idx == N:
        print(*sel)
        return # 리스트를 출력하는 코드
        # for i in range(N):
        #     if sel[i]:
        #         print(arr[i], end  = '')
        # print() # arr을 출력하는 코드
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0 # 초기화
        powerset(idx+1)

powerset(0)