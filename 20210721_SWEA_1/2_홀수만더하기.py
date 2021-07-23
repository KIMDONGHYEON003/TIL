k = int(input())
a = [[0 for j in range(10)] for i in range(0,k)]
c = [0 for i in range(0,k)]
for i in range(0,k):
    for j in range(10):
        a[i][j] = input().split()

        c.append(a)

for i in range(0,k):
    for j in range(10):
        print(f'#{i+1} {c[i]}')