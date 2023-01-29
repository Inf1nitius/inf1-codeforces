s = input().split(", ")

x = set()
y = {"", "{", "}", "{}"}

for i in s:
    if i[0] == "{":
        i = i[1:]
    if i[-1] == "}":
        i = i[:-1]
    x.add(i)

x.difference_update(y)
print(len(x))
