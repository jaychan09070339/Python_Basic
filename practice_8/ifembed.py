#!/usr/bin/python
text=input("请输入1～12个月：")
n=int(text)
if 1<=n<=12:
    print("valid data!")
    if 1<=n<=3:
        print("spring")
    elif 4<=n<=6:
        print("summer")
    elif 7<=n<=9:
        print("autumn")
    else:
        print("winter")
else:
    print("invalid data! Please rewrite again!")
