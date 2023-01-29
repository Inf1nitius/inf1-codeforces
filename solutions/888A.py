n = int(input())
a = input().split()
x = 0

for i in range(len(a)):
    if i > 0 and i < len(a) - 1:
        if int(a[i]) > int(a[i - 1]) and int(a[i]) > int(a[i + 1]):
            x += 1
        elif int(a[i]) < int(a[i - 1]) and int(a[i]) < int(a[i + 1]):
            x += 1

print(x)
