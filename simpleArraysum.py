#!/bin/python3
s = int(input())
res = 0


ab =list(map(int,input().split()))[:s]
for i in range(0,len(ab)):
    res = res + ab[i]

print(res)
