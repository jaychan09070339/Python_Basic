
from random import *
import sys,os
import copy
number=list()
number1=list()
count_A=0
count_B=0
for x in range(4):
	number.append(randrange(0,10))
print("num=",number)
while True:
	num1=int(input("请输入第一个数字："))
	number1.append(num1)
	num2=int(input("请输入第二个数字："))
	number1.append(num2)
	num3=int(input("请输入第三个数字："))
	number1.append(num3)
	num4=int(input("请输入第四个数字："))
	number1.append(num4)
	print("您输入的四个数是：",number1)
	# for x in range(4):
	# 	for y in range(4):
	# 		if number1[x]==number[x]:
	# 			count_A+=1
	# 		elif number1[x]==number[y]:
	# 			if x!=y:
	# 				count_B+=1
	# 			else:
	# 				pass
	for x in range(4):
		if number1[x]==number[x]:
			count_A+=1
			continue
		else:
			for y in range(4):
				number1[x]==number[y]
				count_B+=1
				break
	print(count_A,"A",count_B,"B",sep="")
	count_A=0
	count_B=0
	number1.clear()
    	



