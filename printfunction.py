# The included code stub will read an integer,n
# , from STDIN.
# Without using any string methods, try to print the following: 
#123....n
#Note that "....." represents the consecutive values in between.

print(*range(1,int(input())+1),sep="") # the '*' sign helps in storing the data as an array 
    