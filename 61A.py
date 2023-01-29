a = input()
b = input()
c = "".join("1" if a[i] != b[i] else "0" for i in range(len(a)))


print(c)
