# Consider a list (list = []). You can perform the following commands:

#     insert i e: Insert integer 

# at position
# .
# print: Print the list.
# remove e: Delete the first occurrence of integer
# .
# append e: Insert integer

#     at the end of the list.
#     sort: Sort the list.
#     pop: Pop the last element from the list.
#     reverse: Reverse the list.

# Initialize your list and read in the value of
# followed by lines of commands where each command will be of the types listed above.
#  Iterate through each command in order and perform the corresponding operation on your list. 
#Sample Input 0
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]


#

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




