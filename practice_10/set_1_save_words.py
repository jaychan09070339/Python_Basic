
s=set()
while True:
	words=input("请输入单词：")
	s.add(words)
	if words=="0":
		s.remove("0")
		break
print(s)
print("集合中单词一共有",len(s),"种")


