# 17차시_if.py

a = input()

if a.islower():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.upper(), ord(a.upper())))

elif a.isupper():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.lower(), ord(a.lower())))

else :
   print(a)
