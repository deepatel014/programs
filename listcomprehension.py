#  You are given three integers x,y and z representing the dimensions of a cuboid
# along with an integer n . Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k
# is not equal to n  . Please use list comprehensions rather than
# multiple loops, as a learning exercise.
# Example
# All permutations of are:
# .
# Print an array of the elements that do not sum to .
# Input Format
# Four integers and , each on a separate line.
# Constraints
# Print the list in lexicographic increasing order.
# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0
# Each variable and will have values of or . All permutations of lists in the form
# .
# Remove all arrays that sum to to leave only the valid permutations.
# Sample Input 1
# 2
# 2
# 7/8/2020
# 2/2
# 2
# 2
# Sample Output 1
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1,
# 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2,
# 1], [2, 2, 2]]
#
# 
# 
# # the link to the question is : https://www.hackerrank.com/challenges/list-comprehensions/problem

x,y,z,n = int(input()) ,int(input()),int(input()),int(input())   
print([[a,b,c]for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c != n ])