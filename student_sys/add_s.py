
def add_stu(n):
	for x in range(n):
		name=input("请输入第",x,"个学生的姓名：")
		name_list.append(na)
		age=int(input("请输入第",x,"个学生的年龄："))
		age_list.append(ag)
		score=int(input("请输入第",x,"个学生的成绩："))
		score_list.append(sc)
	d={("姓名","年龄","成绩"):(name_list[x],age_list[x],score_list[x]) for x in range(len(name_list))}
	print(d)