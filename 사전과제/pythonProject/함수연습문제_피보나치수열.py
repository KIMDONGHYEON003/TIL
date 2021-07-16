# 함수연습문제_피보나치수열.py



def fibonacii(k):
   fibo = [1]*k
   for i in range(2 , k):
      fibo[i] = fibo[i-1] + fibo[i-2]
   return fibo

k = int(input())
print(fibonacii(k))