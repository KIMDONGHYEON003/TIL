n = int(input())
cnt = 0
body_lists =[]

for _ in range(n):
    weight, height = map(int, input().split(" "))
    body_lists.append([weight, height])

for idx in range(0, len(body_lists)):
    cnt = 1
    for j in range(0, len(body_lists)):
        if body_lists[idx][0] < body_lists[j][0] and body_lists[idx][1] < body_lists[j][1]:
            cnt+=1
        
    print(cnt, end=" ")