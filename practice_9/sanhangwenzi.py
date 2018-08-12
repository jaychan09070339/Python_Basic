#!/usr/bin/python
#+------+
#| ssss |
#| ssss |
#| ssss |
#+------+
line1=input("请输入第一行：")
line2=input("请输入第二行：")
line3=input("请输入第三行：")
max1=len(line1)
max2=len(line2)
max3=len(line3)
max=max1
if max<max2:
    max=max2
if max<max3:
    max=max3
print("+"+"-"*(max+2)+"+")
print("|"+line1.center(max+2)+"|")
print("|"+line2.center(max+2)+"|")
print("|"+line3.center(max+2)+"|")
print("+"+"-"*(max+2)+"+")
