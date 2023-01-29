n = int(input())
x = input().split()
y = input().split()

del x[0]
del y[0]

z = set()
z.update(x)
z.update(y)

if len(z) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
