

n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]

for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b


result =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):      
    if T[i]+i <= n:       
        result[i] = max(P[i] + result[i + T[i]], result[i+1])   
    else:                
        result[i] = result[i+1]
print(result[0])