n, h = map(int, input().split())
aa = input().split()

l = n

for a in aa:
    if int(a) > h:
        l += 1

print(l)
