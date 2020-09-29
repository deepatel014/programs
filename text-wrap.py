# Input Format
# The first line contains a string,.
# The second line contains the width.

# Output Format
# Print the text wrapped paragraph.
# Sample Input 0
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ




import textwrap


stri = input()
s= int(input())
# print(textwrap.wrap(stri,s))

print(textwrap.fill(stri,s))