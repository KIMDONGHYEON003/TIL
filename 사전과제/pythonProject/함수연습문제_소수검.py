# 함수연습문제_소수검.py

def PrimeNumber(k):
   if k == 1:
      return False

   k_root = round(k**0.5) +1
   for i in range (2, k_root):
      if not (k % i):
         return False
   return True

num = int(input())
if PrimeNumber(num) :
   print("소수입니다.")
else:
   print("소수가 아닙니다.")