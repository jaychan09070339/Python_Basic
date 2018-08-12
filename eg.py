
class Dog:
	def infos(self):
		print(self.kinds,self.color)


dog1=Dog()
dog1.kinds="京巴"
dog1.color="白色"
dog1.infos()

class Student:
	def stu(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score


	def infos(self):
		print(self.name,self.age,self.score)

names=locals()
number=int(input("请输入添加学生的数目："))
for x in range(number):
	name_info=input("请输入学生姓名：")
	age_info=int(input("请输入学生年龄："))
	score_info=int(input("请输入学生成绩："))
	names["student%s"%x]=Student()
	names["student%s"%x].name=name_info
	names["student%s"%x].age=age_info
	names["student%s"%x].score=score_info
for x in range(number):
	names["student%s"%x].infos()

class Human:
	def set_name(self,name):
		self.name=name

	def set_age(self,age):
		self.age=age

	def infos(self):
		print(self.name,self.age)

h1=Human()
h1.set_name("xxx")
h1.set_age(25)
h1.infos()


class Dog1:
	def __init__(self,k,c):
		self.k=k
		self.c=c

dog=Dog("ss","cc")
print(dog.__dict__,dog.__class__,dog.
	__module__)



class car:
	def __init__(self,color,brand,model):
		self.color=color
		self.brand=brand
		self.model=model

	def run(self,speed):
		self.speed=speed
		print(self.color,self.brand,self.model,"在以",self.speed,"km/h速度行驶.",sep="")

	def infos(self):
		print(self.brand,self.model,self.color)

	def change_color(self,c):
		self.color=c

a4=car("红色","奥迪","A4")
a4.run(199)
a4.change_color("黑色")
a4.run(230)