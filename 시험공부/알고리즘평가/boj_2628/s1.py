import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
z_lst = [0]
o_lst = [0]

T = int(input())
cuts = []
for _ in range(T):
    cuts.append(list(map(int,input().split())))

for cut in cuts:
    if cut[0] == 0:             # 가로일 때는 z_lst에 넣는다.
        z_lst.append(cut[1])
    else:                        # 세로일 때는 o_lst에 넣는다.
        o_lst.append(cut[1])

z_lst = sorted(z_lst)
o_lst = sorted(o_lst)
z_lst.append(M)                 # 마지막 컷과 끝 길이를 빼주기 위해
o_lst.append(N)                 # 마지막 컷과 끝 길이를 빼주기 위해

z_result = []
o_result = []
for i in range(len(z_lst)-1):           # z_result, o_result에 짤라서 생긴 길이를 넣는다.
    z_result.append(z_lst[i+1] - z_lst[i])
for i in range(len(o_lst)-1):
    o_result.append(o_lst[i + 1] - o_lst[i])

my_max = 0
for i in range(len(z_result)):      # z_result, o_result에 넣은 값 중에 곱해서 가장 큰 값을 구한다.
    for j in range(len(o_result)):
       if my_max < z_result[i] * o_result[j]:
           my_max = z_result[i] * o_result[j]

print(my_max)
