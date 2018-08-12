
def div_apple(n):
	print("现有",n,"个苹果")
	d=int(input("请输入人数："))
	print("每个人分：",n/d,"个苹果")

try:
	div_apple(10)
except ValueError:
	print("出现值异常！已解决！")
except ZeroDivisionError:
	print("除数为0的错误，已解决！")
except:
	print("程序其他错误！已解决！")

print("程序结束！")