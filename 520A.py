n = int(input())
s = input().lower()

x = set(s)

if len(x) == 26:
    print("YES")
else:
    print("NO")
