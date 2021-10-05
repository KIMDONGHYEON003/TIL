import sys
sys.stdin = open("input.txt")

from itertools import combinations

#주어진 재료들을 조합하여 나오는 음식들의 합
def solution(arr, case):
    result = 0
    for a, b in combinations(case, 2):
        result += arr[a][b] + arr[b][a]     # Sij, Sji 더하면 맛이 결정됨
    return result


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 9999999999999
    cases = list(combinations(range(N), N // 2))

    for case1 in cases:
        case1 = set(case1)
        case2 = set(range(N)) - case1
        result1 = solution(arr, case1)
        result2 = solution(arr, case2)

        if result > abs(result1-result2):
            result = abs(result1-result2)

    print("#{} {}".format(t+1, result))