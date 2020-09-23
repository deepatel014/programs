arr = []
a = (int(input()))

for _ in range(a):
    s = input().split()
    cmd = s[0]
    arg = s[1:]
    if cmd != "print":
        cmd += "("+ ",".join(arg) +")"
        eval("arr."+cmd)
    else:
        print(arr)




print(arr)