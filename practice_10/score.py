#!usr/bin/python
score_C=int(input("请输入语文成绩："))
score_M=int(input("请输入数学成绩："))
score_E=int(input("请输入英语成绩："))
if score_C>score_M:
    if score_M>score_E:
        print(score_C)
        print(score_E)
    else:
        if score_C>score_E:
            print(score_C)
            print(score_M)
        else:
            print(score_E)
            print(score_M)
else:
    if score_M<score_E:
        print(score_E)
        print(score_C)
    else:
        if score_C>score_E:
            print(score_M)
            print(score_E)
        else:
            print(score_M)
            print(score_C)

average=(score_C+score_M+score_E)/3
print(average)
            



