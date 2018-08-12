#!/usr/bin/python
text=input("请输入一个季度1～4个数字：")
n=int(text)
if n==1:
    print("该季度有1月，2月，3月。")
elif n==2:
    print("该季度有4月，5月，6月。")
elif n==3:
    print("该季度有7月，8月，9月。")
elif n==4:
    print("该季度有10月，11月，12月。")
else:
    print("输入数据有误！请重新输入！")

print("程序结束！")
