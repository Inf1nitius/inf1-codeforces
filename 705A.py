n = int(input())
x = []
st = "I "

for i in range(n):
    if i % 2 == 0:
        x.append(0)
    else:
        x.append(1)

for y in x:
    if y == 0:
        st += "hate that I "
    elif y == 1:
        st += "love that I "

print(f"{st[:len(st)-7]}it")
