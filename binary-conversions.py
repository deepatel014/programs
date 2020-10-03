#input:
# 3
# output:
#  1  1  1  1
#  2  2  2 10
#  3  3  3 11


def print_formatted(n):
    for i in range(1,n + 1):
        pad = n.bit_length()
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')

n = int(input())
print_formatted(n)