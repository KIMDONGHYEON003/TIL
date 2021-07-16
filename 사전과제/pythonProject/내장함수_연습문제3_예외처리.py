# 내장함수_연습문제3_예외처리.py

def multiplication(*param):
   result = 1
   for i in param:
      if type(i) != int:
         print("에러발생")
         return
      result *= i
   print(result)

multiplication(1, 2, '4', 3)