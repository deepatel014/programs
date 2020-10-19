#This is an list based program which adds the elements in the list and gives out the sum
s = int(input())

b = input().split()[:s]
count = 0
for i in range(0,len(b)):
    count += int(b[i])


print(count)
