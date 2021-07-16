# 함수연습문제_리스트중복제거.py



def list_to_set(k):
    temp = set(k)
    return list(temp)


k = [1, 2, 3, 4, 3, 2, 1]
print(k)
print(list_to_set(k))