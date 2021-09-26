# 2027_홀수만더하기

k = int(input())
c = [0] * k
a = []
total = 0
for i in range(0,k):
    for j in range(0, 10):
        a = list(map(int, input().split()))
        for num in a:
            if a[num] % 2 != 0 :
                total = total + a[num]
    c[i] = total

for i in range(1,k+1):
    print(f'#{k} {c[i-1]}')
print(a)

