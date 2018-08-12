#!/usr/bin/python
word1 = "A"
word2 = "a"
num1 = ord(word1)
num2 = ord(word2)
count = 0
while count <= 25:
    print(word1,word2,end = "",sep = "")
    num1 + =1
    num2 + =1
    word1 = chr(num1)
    word2 = chr(num2)
    count + = 1

