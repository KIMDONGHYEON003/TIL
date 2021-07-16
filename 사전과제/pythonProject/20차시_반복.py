
# _*_ coding : utf-8 _*_



# 20차시_반복.py


# # step.01
# *
# **
# ***
# ****
#
# for i in range(1,5):
#     print("*"*i)

# i=1
# while i<=4 :
#     print("*"*i)
#     i = i + 1 # 없으면 무한루프 발생



# step.02
# *
# **
# ***
# ****
# *
# **
# ***
# ****
# for i in range(1,3): # 두 번 반복할 수 있음
#     for i in range(1, 5):
#         print("*"*i)

# i, k = 1,1
# while i <=2:
#     while k <=4:
#         print("*" * k)
#         k=k+1
#     k=1 # 안쪽에서 k가 변하기 때문에 k 초기화 구문 필요함.
#     i=i+1


# step.03
# 피라미드
# 첫번째 5개 공백 / -> 점점 하나씩 공백이 줄어듬

i,k=5,1

while i >=0:
    print("{0}{1}".format(" "*i, "*"*(2*k-1)))
    i = i-1
    k = k+1