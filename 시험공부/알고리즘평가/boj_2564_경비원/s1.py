import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split()))
store = int(input())

location = [list(map(int, input().split())) for _ in range(store)]
dong = list(map(int, input().split()))

result = 0

if dong[0] == 1:
    for s_loc in location:
        if s_loc[0] == 1:
            result+=(abs(dong[1] - s_loc[1]))
        elif s_loc[0] == 2:
            result+=(min((M + (N-dong[1]) + (N-s_loc[1])), (M + dong[1] + s_loc[1])))
        elif s_loc[0] == 3:
            result+=(dong[1] + s_loc[1])
        else:
            result+=((N-dong[1]) + s_loc[1])

if dong[0] == 2:
    for s_loc in location:
        if s_loc[0] == 1:
            result+=(min((M + (N - dong[1]) + (N - s_loc[1])), (M + dong[1] + s_loc[1])))
        elif s_loc[0] == 2:
            result+=(abs(dong[1] - s_loc[1]))
        elif s_loc[0] == 3:
            result+=(dong[1] + (M - s_loc[1]))
        else:
            result+=((N - dong[1]) + (M - s_loc[1]))

if dong[0] == 3:
    for s_loc in location:
        if s_loc[0] == 1:
            result+=(dong[1] + s_loc[1])
        elif s_loc[0] == 2:
            result+=((M-dong[1]) + s_loc[1])
        elif s_loc[0] == 3:
            result+=(abs(dong[1] - s_loc[1]))
        else:
            result+=(min((N + s_loc[1] + dong[1]), (N + (M - s_loc[1]) + (M - dong[1]))))
elif dong[0] == 4:
    for s_loc in location:
        if s_loc[0] == 1:
            result+=(dong[1] + (N - s_loc[1]))
        elif s_loc[0] == 2:
            result+=((M-dong[1]) + (N - s_loc[1]))
        elif s_loc[0] == 3:
            result+=(min((N + s_loc[1] + dong[1]), (N + (M - s_loc[1]) + (M - dong[1]))))
        elif s_loc[0] == 4:
            result+=(abs(dong[1] - s_loc[1]))
print(result)