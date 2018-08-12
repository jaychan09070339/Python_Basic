
from random import *
flower=list()
puk=list()
puk_1=list()
heitao=chr(ord("\u2660"))
meihua=chr(ord("\u2663"))
fangkuai=chr(ord("\u2665"))
hongtao=chr(ord("\u2666"))
flower=[heitao,meihua,fangkuai,hongtao]
for x in range(4):
	for y in range(1,14):
		if y==1:
			y="A"
		elif y==11:
			y="J"
		elif y==12:
			y="Q"
		elif y==13:
			y="K"
		else:
			pass
		puk.append(flower[x]+str(y))
puk.append("DW")
puk.append("XW")
# print(puk)
shuffle(puk)
# print(puk)
for x in range(3):
	num=choice(puk)
	puk_1.append(num)
	puk.remove(num)
	# print(num,end=" ")
text1=input("即将输出第1个人的十七张牌！")
print([puk[x] for x in range(17)])
text2=input("即将输出第2个人的十七张牌！")
print([puk[x] for x in range(18,34)])
text3=input("即将输出第3个人的十七张牌！")
print([puk[x] for x in range(35,51)])
text4=input("即将输出底牌三张！")
print(puk_1)
