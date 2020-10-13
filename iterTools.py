# Sample Input

#  1 2
#  3 4

# Sample Output

#  (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import product

mylist1 = []
mylist2 =[]

#taking input
s=input().split() 
two=input().split()
#iterating through the input and passing into another list with int type
for i in s:
    mylist1.append(int(i))

for j in two:
    mylist2.append(int(j))

#passing the product of the two lists into l5
l5=list(product(mylist1,mylist2))

#printing the list
for i in range(0,len(l5)):
    print(l5[i],end =' ')
