#!/usr/bin/python
text=input("请输入字符：")
print(text.count("a"))

count=0
for ch in text:
    if ch=="a":
        count+=1
print(count)


