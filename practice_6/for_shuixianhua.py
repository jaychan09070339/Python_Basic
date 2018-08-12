#!/usr/bin/python
for num in range(100,1000):
    bai=num//100
    shi=num%100//10
    ge=num%10
    if num==bai**3+shi**3+ge**3:
        print(num)

