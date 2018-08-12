
key=list()
name_list=list()
age_list=list()
for x in range(5):
    name=input("请输入姓名：")
    text_age=input("请输入年龄：")
    age=int(text_age)
    name_list.append(name)
    age_list.append(age)
dic={name_list[i]:age_list[i] for i in range(5)}
print(dic)
age_i=int(input("请输入需要打印的年龄："))
for x in dic.items():
	if x[1]<age_i:
		print(list(x))