#!/usr/bin/python
#计算北京出租车计价器
distance=int(input("请输入公里数："))
if distance>0:
    if 0<=distance<=3:
        print("费用13元")
    elif 3<distance<=15:
        price=13+2.3*(distance-3)
        print(price)
    else:
        price=(13+2.3*15)+(1+0.5)*(distance-15)*2.3
        print(price)
else:
    print("非法数据！请重新输入！")

