
from time import *

def cal_birthdate(*args):
	return mktime(*args)

Exp=list()
Text=input("请输入出生日期，按<回车>开始输入：")
year=int(input("请输入年："))
month=int(input("请输入月："))
day=int(input("请输入日："))
hour=int(input("请输入时："))
minute=int(input("请输入分："))
second=int(input("请输入秒："))
week=int(input("请输入星期数："))
yd_birth=int(input("请输入距离元旦天数："))

Exp.append(year)
Exp.append(month)
Exp.append(day)
Exp.append(hour)
Exp.append(minute)
Exp.append(second)
Exp.append(week-1)
Exp.append(yd_birth)
Exp.append(0)

par=tuple(Exp)
cal_1=cal_birthdate(par)
local_time=time()+8*3600
diff=local_time-cal_1
day_2=diff//3600//24
print("出生至今已经过去",day_2,"天")