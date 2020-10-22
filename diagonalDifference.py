# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12

# Sample Output

# 15

# Explanation

# The primary diagonal is:

# 11
#    5
#      -12

# Sum across the primary diagonal: 11 + 5 - 12 = 4

# The secondary diagonal is:

#      4
#    5
# 10

# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15

# Note: |x| is the absolute value of x
arr = []

r = int(input())
for _ in range(r):
    arr.append(list(map(int,input().rstrip().split())))


ldiag = sum([arr[x][x] for x in range(r)])
rdiag = sum([arr[x][r-1-x] for x in range(r)])

print(abs(ldiag-rdiag))
        