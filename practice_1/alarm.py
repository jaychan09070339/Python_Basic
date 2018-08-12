
from time import *
hour=input("请输入闹铃小时设定时间：")
minute=input("请输入闹铃分钟设定时间：")
text=hour+":"+minute+":"+"00"
while True:
	if text==strftime("%H:%M:00"):
		break
while True:
	for x in range(1,61):
		print("时间到了！")
		sleep(1)
	break


	



