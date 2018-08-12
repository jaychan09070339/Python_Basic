
s=input("请输入一段字符串或数字：")
# n=len(s)//2
# for x in range(0,n+1):
# 	if s[x]!=s[-(x+1)]:
# 		print("不是")
# 		break
# else:
#     print("是")


# l=list(s)
# l2=list(reversed(s))
# if l==l2:
# 	print("是")
# else:
# 	print("不是")

if s==s[::-1]:
	print("是")
else:
	print("不是")