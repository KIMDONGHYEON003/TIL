import sys
import copy
sys.stdin = open("input.txt")

T = int(input())

for num in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col_arr = list(zip(*arr))
    col_array = []
    for col in col_arr:
        col = list(col)
        col_array.append(col)
    result = []
    tmp = []

    tmp = copy.deepcopy(col_array)


    for x in range(len(col_array)):
        for y in range(len(col_array[x])):
            if col_array[x][y] in result:
                for _ in range(tmp[x].count(col_array[x][y])):
                    tmp[x].remove(col_array[x][y])
            else:
                result.append(min(tmp[x]))

    result = set(result)
    print("#{} {}".format(num+1, sum(result)))


