# 함수연습문제_가위바위보

list = ["가위", "바위", "보"]


def Check(a, b):
    if (a == b):
        print("비겼습니다!")
    elif (a == list[0] and b == list[1]) or (b == list[0] and a == list[1]):
        print("바위가 이겼습니다!")
    elif (a == list[0] and b == list[2]) or (b == list[0] and a == list[2]):
        print("가위가 이겼습니다!")
    elif (a == list[1] and b == list[2]) or (b == list[1] and a == list[2]):
        print("보가 이겼습니다!")


name1, name2 = input(), input()
t1, t2 = input(), input()
Check(t1, t2)