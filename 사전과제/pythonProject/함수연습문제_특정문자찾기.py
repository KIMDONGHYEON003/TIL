# 함수연습문제_특정문자찾기.py

def tf(k, t) :
   print("%d => " % t, end = "")
   if t in k :
      print(True)
   else:
      print(False)

k = [2, 4, 6, 8, 10]
print(k)
tf(k, 5)
tf(k, 10)