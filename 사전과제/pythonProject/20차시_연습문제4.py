# 20차시_연습문제4.py

result = ""
for i in range(1, 101):
   if i & 1:
      result += "%d, " % i
print(result[0:len(result)-2])