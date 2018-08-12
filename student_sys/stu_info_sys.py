
import sys,os
import copy
name_list=list()
age_list=list()
score_list=list()
d=dict()

score_list_0=list()
name_list_0=list()
age_list_0=list()
score_index=list()

score_list_1=list()
name_list_1=list()
age_list_1=list()
score_index_1=list()

def view():
	text=input("欢迎来到学生信息管理系统！按回车键进入！")
	print("+"+"-"*(32)+"+")
	print("|"+"1):添加学生信息"+" "*17+"|")
	print("|"+"2):显示所有学生信息"+" "*13+"|")
	print("|"+"3):删除学生信息"+" "*17+"|")
	print("|"+"4):修改学生成绩"+" "*17+"|")
	print("|"+"5):按学生成绩高低显示学生信息"+" "*3+"|")
	print("|"+"6):按学生成绩低高显示学生信息"+" "*3+"|")
	print("+"+"-"*(32)+"+")

def view_2(name_l,age_l,score_l):
	max_name=vs(name_l)
	max_age=vs2(age_l)
	max_score=vs2(score_l)
	m1=vs_1(max_name)
	m2=vs_2(max_age)
	m3=vs_2(max_score)
	print("+"+"-"*(m1+4)+"+"+"-"*(m2+4)+"+"+"-"*(m3+4)+"+")
	print("|"+"姓名".center(m1+2)+"|"+"年龄".center(m2+2)+"|"+"成绩".center(m3+2)+"|")
	print("+"+"-"*(m1+4)+"+"+"-"*(m2+4)+"+"+"-"*(m3+4)+"+")
	for x in range(len(name_l)):
		print("|"+str(name_l[x]).center(m1+4)+"|"+str(age_l[x]).center(m2+4)+"|"+str(score_l[x]).center(m3+4)+"|")
	print("+"+"-"*(m1+4)+"+"+"-"*(m2+4)+"+"+"-"*(m3+4)+"+")





def vs(list_l):
	max_m=len((list_l[0]))
	for x in range(len(list_l)):
		if max_m<len(list_l[x]):
			max_m=len(list_l[x])
		else:
			pass
	return max_m

def vs2(list_l):
	max_m=len(str(list_l[0]))
	for x in range(len(name_list)):
		if max_m<len(str(list_l[x])):
			max_m=len(str(list_l[x]))
		else:
			pass
	return max_m


def vs_1(m):
	if m<2:
		m=4
	else:
		pass
	return m

def vs_2(n):
	if n<3:
		n=6
	else:
		pass
	return n

def add_stu(n):
	for x in range(n):
		name=input("请输入学生的姓名：")
		age=int(input("请输入学生的年龄："))
		score=int(input("请输入学生的成绩："))
		name_list.append(name)
		age_list.append(age)
		score_list.append(score)
	# text_11=input("是否继续添加？Y or N?")
	# if text_11=="y" or "Y":
	# 	n=int(input("请输入增加学生人数："))
	# 	add_stu(n)
	# else:
	print("表格如下所示：")
	show_info(name_list,age_list,score_list)
	return name,age,score

def show_info(name_l,age_l,score_l):
	view_2(name_l,age_l,score_l)


def del_info(text1):
	index_name=name_list.index(text1)
	# print(index_name)
	name_list.remove(name_list[index_name])
	age_list.remove(age_list[index_name])
	score_list.remove(score_list[index_name])
	print("当前信息表情况如下：")
	

def modify_info(text2):
	index_name=name_list.index(text2)
	text_age=int(input("请输入修改的同学的年龄："))
	text_score=int(input("请输入修改的同学的分数："))
	del_info(text2)
	name_list.insert(index_name,text2)
	age_list.insert(index_name,text_age)
	score_list.insert(index_name,text_score)
	

def score_sort_little_2_more():
	score_list_0=copy.deepcopy(score_list)
	score_list_0.sort()
	for x in score_list_0:
		score_index.append(score_list.index(x))
	for y in score_index:
		name_list_0.append(name_list[y])
		age_list_0.append(age_list[y])
	view_2(name_list_0,age_list_0,score_list_0)

def score_sort_more_2_little():
	score_list_1=copy.deepcopy(score_list)
	score_list_1.sort(reverse=True)
	for x in score_list_1:
		score_index_1.append(score_list.index(x))
	for y in score_index_1:
		name_list_1.append(name_list[y])
		age_list_1.append(age_list[y])
	view_2(name_list_1,age_list_1,score_list_1)



def main():
	while True:
		view()
		number=input("请输入选项（1-6）：请按q退出系统！")
		if number=="1":
			n=int(input("请输入增加学生人数："))
			add_stu(n)
			t=input("返回上一层请按回车键！")
			m_ain()
		if number=="2":
			show_info(name_list,age_list,score_list)
			t=input("返回上一层请按回车键！")
			m_ain()
		if number=="3":
			show_info(name_list,age_list,score_list)
			text_1=input("请输入要删除的学生的姓名：")
			del_info(text_1)
			show_info(name_list,age_list,score_list)
		if number=="4":
			show_info(name_list,age_list,score_list)
			text_2=input("请输入要修改的学生的姓名：")
			modify_info(text_2)
			show_info(name_list,age_list,score_list)
		if number=="5":
			score_sort_more_2_little()
		if number=="6":
			score_sort_little_2_more()
		if number=="q":
			sys.exit(0)
		else:
			pass


if __name__=="__main__":
	main()


