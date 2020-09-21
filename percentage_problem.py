n = int(input())
dic = {}
for _ in range(n):
    name,*line = input().split()
    scores = list(map(float,line))
    dic[name] = scores

query = input()

tot = sum(dic[query])   
avg = tot/3
print("%.2f"%(avg))