
text=input("请输入字符：")
exist=[]
for x in text:
	if x not in exist:
		print(x,"出现",text.count(x),"次")
		exist.append(x)

# 获取数字
# for x in range(10):
# 	if str(x) in text:
		# print(x,"出现",text.count(str(x)),"次")