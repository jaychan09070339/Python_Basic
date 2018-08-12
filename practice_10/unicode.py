
start=int(input("请输入起始值："))
end=int(input("请输入终止值："))
s="十进制编码 十六进制编码     文字"
lenth=len(s)
x=start
print(s.center(13))
for num in range(start,end+1):
    print(str(num).center(5),end=" ",sep="")
    print(str(hex(num)).center(20),end=" ",sep=" ")
    print(chr(num).center(5),end=" ",sep=" ")
    print()
