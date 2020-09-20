#Problem Statement:
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n
# scores. Store them in a list and find the score of the runner-up.
#
#  Input Format
# The first line contains n
# . The second line contains an array arr [] of n
# integers each separated by a space.
# 
# Output Format
# Print the runner-up score.
# 
# Sample Input 0
# 5
# 2 3 6 6 5
# 
# Sample Output 0
# 5
#
# a= int(input())
# arr = list(map(int,input().strip().split())) [:a]
# z = max(arr)  #//gets the max of the array
# for i in range(a):
#     if max(arr) == z:
#         arr.remove(z)
# print(max(arr))

a= int(input())

arr =[]
for i in range(a):
    z = int(input())
    arr.append(z)

print(arr)