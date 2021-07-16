# 20차시_연습문제5.py
#tot=0
# for i in range(1,101):
#     if i % 3 ==0:
#         tot = tot + i
# print("1부터 100사이의 숫자 중 3의 배수의 총합:%d" % tot)


result = 0
for i in range(1, 101):
   if not (i % 3):
      result += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(result))
