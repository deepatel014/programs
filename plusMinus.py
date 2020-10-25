
#Sample Input

#6
#-4 3 -9 0 4 1         

#Sample Output

#0.500000
#0.333333
#0.166667

n = float(input())
lst = [int(x) for x in input().split()]
print(format(len([x for x in lst if x > 0])/n, ".6f"))
print(format(len([x for x in lst if x < 0])/n, ".6f"))
print(format(len([x for x in lst if x == 0])/n, ".6f"))
