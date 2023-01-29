n = int(input())
x = set()
y = []
z = {1: "YES", 0: "NO"}

for i in range(n):
    i = input()
    if i in x:
        y.append(1)
    else:
        y.append(0)
        x.add(i)

for i in y:
    print(z.get(i))
