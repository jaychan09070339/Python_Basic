
name_list=[]
age_list=[]
ln=list()
la=list()
for x in range(5):
    name=input("请输入姓名：")
    text_age=input("请输入年龄：")
    lnn=len(name)#算出字符串姓名的长度
    ln.append(lnn)#将姓名字符串长度添加到ln列表
    age=int(text_age)
    la.append(len(text_age))
    name_list.append(name)
    age_list.append(age)
print("name:",name_list)
print("age:",age_list)
print("name_length:",ln)
print("age_length:",la)
print()
ln.sort()
la.sort()
name_max=ln[4]
age_max=la[4]
if ln[4]<6:
    name_max=6
if la[4]<6:
    age_max=6
# print(ln[4])
# print(la[4])
print("+"+"-"*(name_max+4)+"+"+"-"*(age_max+4)+"+")
print("|"+"姓名".center(name_max+2)+"|"+"年龄".center(age_max+2)+"|")
print("+"+"-"*(name_max+4)+"+"+"-"*(age_max+4)+"+")
for x in range(5):
    print("|"+name_list[x].center(name_max+4)+"|"+str(age_list[x]).center(age_max+4)+"|")

print("+"+"-"*(name_max+4)+"+"+"-"*(age_max+4)+"+")

