arr = [1,5,25,3,5,8,4,5,21,1,5,10]

def Counting(arr, result, k):
    C = [0] * (k + 1)

    for i in range(0, len(arr)): # 카운팅할 배열에 index 값과 arr의 요소값을 맞춰서 C배열에 요소값에 카운팅해서 입력
        C[arr[i]] += 1

    for i in range(1, len(C)):  # C 배열을 돌면서 하나씩 누적해준다.
        C[i] += C[i-1]          # result 배열에 알맞는 index를 찾아가게 하기 위해

    for i in range(0,len(arr)):
        C[arr[i]] -= 1                  # C에서 카운팅 해준 값을 하나씩 빼준다.
        result[C[arr[i]]] = arr[i]      # C 요소값이 result의 index로 찾아 들어가며 arr[i] 값을 입력해준다.
    return result

k = max(arr)
result = [0 for _ in range(len(arr))]

print(Counting(arr, result, k))
