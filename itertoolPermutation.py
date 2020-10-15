# This code uses the permutation function from the itertools library 

# Sample Input

# #HACK 2

# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH


from itertools import permutations
a,size = input().split()
a=a.upper()
b = list(permutations(a,int(size)))
b.sort()
for i in range(0,len(b)):
    for j in b[i]:
        print(j,end ='')
    print()