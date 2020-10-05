#this code basically takes in nput from the user
#and changes the first letter of each word into uppercase

#input:
# charlie angel

#output:
#Charlie Angel

a=input()
newstring = ""
lis = list(a.split())
for i in lis:
    newstring += i.capitalize()+" "

print(newstring)


#alternae code from hackerRank:
# s = input()
# for x in s[:].split():
#     s = s.replace(x, x.capitalize())
# print(s)