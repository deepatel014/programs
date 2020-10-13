def merge_tool(string,z):
    while string:
        seen = string[0:z]
        s = ''
        for c in seen:
            if c not in s:
                s += c
        print(s)
        string = string[z:]



s = input()
i = int(input())
merge_tool(s,i)