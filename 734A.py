n = int(input())
s = input()
a = 0
d = 0

for l in s:
    if l == "A":
        a += 1
    else:
        d += 1

if a > d:
    print("Anton")
elif a == d:
    print("Friendship")
else:
    print("Danik")
