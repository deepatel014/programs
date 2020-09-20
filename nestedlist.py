#
#Given the names and grades for each student in a class of
# students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
#
# Sample Input 0
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0

# Berry
# Harry

a = int(input())

arr = [[input(),float(input())] for _ in range(a)]

arr2 = sorted(list(set([marks for name,marks in arr])))[1]

print("\n".join([a for a,b in sorted(arr) if b == arr2]))
