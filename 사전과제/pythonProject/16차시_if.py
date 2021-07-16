# 16차시_if.py

a = ['가위','바위','보']

man1 = input()
man2 = input()

if man1 == a[0]:
    if man2 == a[0]:
        print("Result : Draw")
    if man2 == a[1]:
        print("Result : Man2 Win!")
    if man2 == a[2]:
        print("Result : Man1 Win!")
if man1 == a[1]:
    if man2 == a[0]:
        print("Result : Man1 Win!")
    if man2 == a[1]:
        print("Result : Draw")
    if man2 == a[2]:
        print("Result : Man2 Win!")
if man1 == a[2]:
    if man2 == a[0]:
        print("Result : Man2 Win!")
    if man2 == a[1]:
        print("Result : Man1 Win!")
    if man2 == a[2]:
        print("Result : Draw")
