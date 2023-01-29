n = input()
i = sum(int(x) in {4, 7} for x in n)

if i in [4, 7]:
    print("YES")
else:
    print("NO")
