string = input()
new = list(string.split())
vowels = ['A','E','I','O','U']

kev = 0
stu = 0

for i in new:
    if i in vowels:
        kev +=len(new)-1
    else:
        stu +=len(new)-1

if kev > stu:
    print("Kevin {}".format(kev))
elif kev < stu:
    print("Stuart {}".format(stu))
else:
    print("Draw")
