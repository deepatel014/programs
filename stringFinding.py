#Basically it is a function that shows howmwny times a crtain string has been repeated in a string
string= input()
f = input()
count = 0
for i in range(0,len(string)+1):
    if f == string[i:i+len(f)]:
        count+=1

print(count)