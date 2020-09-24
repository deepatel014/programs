a = int(input())
tu = list([int(input().strip().split())]for _ in range(a))
tup= tuple(tu)
print(hash(tup))