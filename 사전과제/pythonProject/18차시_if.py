# 18차시_if.py



result = ""
for i in range(1, 201):
   if not (i % 7) and (i % 5):
      result += "%d," % i
print(result[0:len(result)-1])