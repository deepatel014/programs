# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# Input Format
# The first line contains a string consisting of space separated words.
# Output Format
# Print the formatted string as explained above.

# Sample Input:
# this is a string   

# Sample Output:
# this-is-a-string

def split_and_join(line):
    b = line.split()
    c = "-".join(b)
    return c
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
