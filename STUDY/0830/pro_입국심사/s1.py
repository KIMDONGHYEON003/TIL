def solution(n, times):
    right = max(times) * n
    left = 1

    answer = binary(left, right)
    return answer

def binary(start, end):
    mid = (start + end) // 2
    count = 0
    for t in times:
        count += mid // t
        # 심사한 사람 수를 구하기 위해 총 시간에서 각각 시간을 나눔

    # count가 더 크면 시간을 줄여야하기 때문에 앞쪽으로 간다
    # count가 작으면 전부 심사를 못했기 때문에 뒷쪽으로 간다
    if count == n:
        return mid
    elif count < n:
        return binary(mid + 1, end)
    elif count > n:
        return binary(start, mid - 1)

import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")

n = int(input())
times = list(map(int, input().split()))

print(solution(n, times))