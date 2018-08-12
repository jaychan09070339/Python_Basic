
s=input("请输入一个数字或一个字符串：")
length=len(s)
count=0
if length%2==0:
	for i in range(0,length//2):
		if s[i]==s[length-i-1]:
			count+=1
		else:
			print(s,"不是回文串")
			break
	if count==length//2:
		print(s,"是回文串")
else:
	for j in range(0,length//2+1):
		if s[j]==s[length-j-1]:
			count+=1
		else:
			print(s,"不是回文串")
			break
	if count==length//2+1:
		print(s,"是回文串")

print("程序结束！")