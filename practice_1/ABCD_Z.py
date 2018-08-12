#!/usr/bin/python
word="A"
num=ord(word)
count=0
while count<=25:
    print(word,end="")
    num+=1
    word=chr(num)
    count+=1

