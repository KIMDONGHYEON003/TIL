k = input()
c= [0 for i in range(k)]
for i in range(0,k):
    a= list(map(int, input().split()))

    a[0]=int(a[0])
    a[1]=int(a[1])

    if a[0] >9 or a[1] > 9:
        c[i] = -1
    else:
        c[i] = a[0] * a[1]

for i in range(1,k+1):
    print(f'#{i} {c[i-1]}')