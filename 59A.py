s = input()
i = 0

for l in s:
    if l.isupper():
        i += 1
    else:
        i -= 1

if i > 0:
    print(s.upper())
else:
    print(s.lower())
