
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    acount = 0
    bcount = 0
    for i in range(0,len(a)):
        if a[i]>b[i]:
            acount +=1
        elif a[i]<b[i]:
            bcount +=1
        else:
            acount += 0
            bcount += 0
    return "{}{}".format(acount,bcount)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
