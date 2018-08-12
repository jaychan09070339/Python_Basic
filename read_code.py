
f=open("gb2312.txt","rb")
b=f.read()
s=b.decode("utf-8")
print(s)
f.close()