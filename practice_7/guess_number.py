
from random import *
import sys,os
x=randrange(1,101)
count=0
while True:
	num=int(input("请输入一个数字："))
	if num==x:
		print("恭喜您！猜对了！")
		print("您一共猜了",count,"次")
		sys.exit(0)
	if num<x:
		print("您猜的数小了，请重新猜！")
		count+=1
	if num>x:
		print("您猜的数大了，请重新猜！")
		count+=1
